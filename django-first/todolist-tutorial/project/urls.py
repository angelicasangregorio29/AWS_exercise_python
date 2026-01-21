from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # GET
    path("add", views.add_project, name="add_project"), # GET
]