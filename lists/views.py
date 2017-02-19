from django.shortcuts import render
from django.utils import timezone


def home_page(request):
    return render(request, "home_page.html", {})
