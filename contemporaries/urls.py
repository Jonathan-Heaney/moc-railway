from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("generate-random/", views.generate_random, name="generate-random")
]
