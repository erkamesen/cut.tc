from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse 
from api.models import BaseURL, RedirectURL
from rest_framework.generics import get_object_or_404
# Create your views here.


def router(request, slug):
    url = get_object_or_404(BaseURL, short_code=slug)
    base_url = url.base_url
    return redirect(base_url)
    
