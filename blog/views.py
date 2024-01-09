from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_blog(request):
    return HttpResponse("Hello, Blog!")

def test_route(request):
    return HttpResponse("Test Route!")