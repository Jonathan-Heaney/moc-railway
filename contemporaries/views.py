from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import os
from .models import FamousPerson
import random
import urllib.parse
from collections import namedtuple


# Create your views here.


@require_POST
def set_generation_flag(request):
    request.session['generate_person'] = True
    request.session['hpi_threshold'] = request.POST.get(
        'hpi', 50)  # Default to 50 if not provided
    return redirect('main-page')


@require_POST
def find_contemporaries(request):
    person_id = request.POST.get('person_id')
    request.session['chosen_person_id'] = person_id
    return redirect('main-page')


def search_person(request):
    query = request.GET.get('q', '').strip()
    if len(query) >= 3:
        people = FamousPerson.objects.filter(
            name__icontains=query).values('id', 'name', 'birthyear', 'deathyear')[:10]
        if people:
            return JsonResponse({'results': list(people)})
        else:
            # No results found
            return JsonResponse({'message': 'No people found'})
    return JsonResponse({'results': []})  # Empty or too short query


def select_person(request, person_id):
    request.session['chosen_person_id'] = person_id
    return redirect('main-page')


def main_page(request):
    generate_person = request.session.pop('generate_person', False)
    chosen_person_id = request.session.pop('chosen_person_id', None)
    hpi_threshold = int(request.session.pop('hpi_threshold', '50'))

    if generate_person:
        # The flag was set, generate random person
        random_person_data = random_person(request, hpi_threshold)
        chosen_person_id = random_person_data["id"]
    elif chosen_person_id:
        # Logic to fetch the chosen person's data if an ID is provided
        random_person_data = get_person_by_id(chosen_person_id)
    else:
        # The flag was not set or has been cleared, show default state
        random_person_data = None

    # If we have a person (randomly generated or chosen), generate overlaps
    if chosen_person_id:
        top_overlaps_data = top_overlap(request, chosen_person_id)
        fame_overlaps_data = fame_overlap(request, chosen_person_id)
    else:
        top_overlaps_data = fame_overlaps_data = None

    return render(request, "contemporaries/index.html", {
        "person": random_person_data,
        "top_overlaps": top_overlaps_data,
        "fame_overlaps": fame_overlaps_data,
        "hpi_threshold": hpi_threshold,
    })


# Function to retrieve a random person from the database
def random_person(request, min_hpi):
    # Get the minimum hpi from request parameters, default to 50 if not provided
    #  min_hpi = int(request.GET.get('min_hpi', 50))
    valid_persons_above_threshold = FamousPerson.objects.filter(
        hpi__gte=min_hpi)
    valid_person_count = valid_persons_above_threshold.count()
    random_index = random.randint(0, valid_person_count - 1)
    person = valid_persons_above_threshold[random_index]

    # Utilize the prepare_person_data function to construct response data
    response_data = prepare_person_data(person)

    return response_data


def get_person_by_id(person_id):
    try:
        person = FamousPerson.objects.get(id=person_id)
        response_data = prepare_person_data(person)
        return response_data
    except FamousPerson.DoesNotExist:
        return None


OverlapResult = namedtuple(
    'OverlapResult', ['percentage', 'start', 'end', 'years'])


def calculate_overlap(person1, person2):
    latest_start = max(person1.birthyear, person2.birthyear)
    earliest_end = min(person1.deathyear, person2.deathyear)
    overlap_years = max(0, earliest_end - latest_start)
    person1.lifespan = person1.deathyear - person1.birthyear
    percentage = (overlap_years / person1.lifespan) * \
        100 if person1.lifespan > 0 else 0
    percentage = round(percentage, 2)

    return OverlapResult(percentage, latest_start, earliest_end, overlap_years)


def prepare_person_data(person, extra_data=None):
    extra_data = extra_data or {}
    wikipedia_link = generate_wikipedia_link(person.name)
    formatted_lifespan = format_lifespan(person.birthyear, person.deathyear)
    person_data = {
        'id': person.id,
        'name': person.name,
        'occupation': person.occupation,
        'birthyear': person.birthyear,
        'deathyear': person.deathyear,
        'lifespan': formatted_lifespan,
        'hpi': person.hpi,
        'wikipedia_link': wikipedia_link,
    }
    person_data.update(extra_data)
    return person_data


def calculate_overlaps(chosen_person, score_func):
    all_people = FamousPerson.objects.exclude(id=chosen_person.id)
    overlaps = []

    for person in all_people:
        overlap_result = calculate_overlap(chosen_person, person)
        score = score_func(overlap_result, person)
        overlaps.append((person, score, overlap_result))

    return overlaps


def overlap_score(overlap_result, person):
    return overlap_result.percentage


def fame_overlap_score(overlap_result, person):
    return overlap_result.percentage * (person.hpi ** 10)


def top_overlap(request, person_id):
    chosen_person = FamousPerson.objects.get(id=person_id)
    overlaps = calculate_overlaps(chosen_person, overlap_score)
    overlaps.sort(key=lambda x: x[1], reverse=True)
    top_overlaps = overlaps[:10]

    response_data = [prepare_person_data(person, {
        'overlap_score': score,
        'percentage': overlap_result.percentage,
        'overlap_string': format_lifespan(overlap_result.start, overlap_result.end),
        'years': overlap_result.years,
    }) for person, score, overlap_result in top_overlaps]

    return response_data


def fame_overlap(request, person_id):
    chosen_person = FamousPerson.objects.get(id=person_id)
    fame_overlaps = calculate_overlaps(chosen_person, fame_overlap_score)
    fame_overlaps.sort(key=lambda x: x[1], reverse=True)
    top_fame_overlaps = fame_overlaps[:10]

    response_data = [prepare_person_data(person, {
        'fame_overlap_score': score,
        'percentage': overlap_result.percentage,
        'overlap_string': format_lifespan(overlap_result.start, overlap_result.end),
        'years': overlap_result.years,
    }) for person, score, overlap_result in top_fame_overlaps]

    return response_data


# Function to generate Wikipedia links for famous people
def generate_wikipedia_link(name):
    formatted_name = urllib.parse.quote(name.replace(" ", "_"))
    return f"https://en.wikipedia.org/wiki/{formatted_name}"


def format_lifespan(birthyear, deathyear):
    if birthyear > 0:
        return f"{birthyear} - {deathyear}"

    formatted_birthyear = format_year(birthyear)
    formatted_deathyear = format_year(deathyear)

    return f"{formatted_birthyear} - {formatted_deathyear}"


def format_year(year):
    if year < 0:
        return f"{abs(year)} BC"
    else:
        return f"{year} AD"
