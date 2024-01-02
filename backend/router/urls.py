from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("<slug:slug>/", view=views.router, name="router")
]