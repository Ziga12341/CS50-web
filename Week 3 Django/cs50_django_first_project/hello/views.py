from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    return render(response, "hello/index.html")


def ziga(response):
    return HttpResponse("Hello Žiga")


def greet(response, name):
    return render(response, f"hello/greet.html", {
        "name": name.capitalize()
    })