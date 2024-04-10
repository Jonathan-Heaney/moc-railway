from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main-page"),
    path("generate/", views.set_generation_flag, name='set-generation-flag'),
    path("find-contemporaries/", views.find_contemporaries,
         name='find-contemporaries')
]
