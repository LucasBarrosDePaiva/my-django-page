from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/pages/home.html')


def contact(request):
    return HttpResponse('Contact')


def about(request):
    return HttpResponse('About')


# Create your views here.
