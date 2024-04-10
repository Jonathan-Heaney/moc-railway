from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main-page"),
    path("generate/", views.set_generation_flag, name='set-generation-flag'),
    path("find-contemporaries/", views.find_contemporaries,
         name='find-contemporaries'),
    path('select-person/<int:person_id>/',
         views.select_person, name='select-person'),
    path('search-person/', views.search_person, name='search-person')
]
