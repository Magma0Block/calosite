from django.http import HttpResponse
from django.shortcuts import render


def index_page(request):
    context = {}

    return render( request, "index.html", context)