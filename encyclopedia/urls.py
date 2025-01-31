from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random", views.randomPage, name="random")
]
