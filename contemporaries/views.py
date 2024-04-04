from django.shortcuts import render
import os
from .models import FamousPerson
import random
import urllib.parse

# Create your views here.


# Function to generate Wikipedia links for famous people
def generate_wikipedia_link(name):
    formatted_name = urllib.parse.quote(name.replace(" ", "_"))
    return f"https://en.wikipedia.org/wiki/{formatted_name}"


def index(request):
    return render(request, "contemporaries/index.html")
