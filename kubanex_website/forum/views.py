from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'forum/index.html', {})


def sign_up(request):
    return render(request, 'forum/registration.html', {})

# Create your views here.
