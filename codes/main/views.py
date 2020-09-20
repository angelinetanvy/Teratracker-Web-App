from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response,"main.html")

def out(response):
    return render(response, "out.html")

