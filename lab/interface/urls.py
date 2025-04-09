from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("status", views.status, name="status"),
    path("branches", views.branches, name="branches"),
    path("contact", views.contact, name="contact"),
    path("lists", views.lists, name="lists"),
]