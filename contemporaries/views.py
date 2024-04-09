from django.shortcuts import render
import os
from .models import FamousPerson
import random
import urllib.parse


valid_persons = FamousPerson.objects.exclude(
    birthyear__isnull=True
).exclude(
    deathyear__isnull=True
)

person_count = valid_persons.count()


# Create your views here.


# Function to generate Wikipedia links for famous people
def generate_wikipedia_link(name):
    formatted_name = urllib.parse.quote(name.replace(" ", "_"))
    return f"https://en.wikipedia.org/wiki/{formatted_name}"


def index(request):
    random_index = random.randint(0, person_count - 1)
    person = valid_persons[random_index]
    return render(request, "contemporaries/index.html", {
        "person": person,
        "wikipedia_link": generate_wikipedia_link(person.name)
    })


