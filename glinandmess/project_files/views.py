from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):
    context = {}
    return render(request, "index.html", context)


def about_page(request):
    context = {}
    return render(request, "about.html", context)


def rent_page(request):
    context = {}
    return render(request, "rent.html", context)


def revs_page(request):
    context = {}
    return render(request, "revs.html", context)
