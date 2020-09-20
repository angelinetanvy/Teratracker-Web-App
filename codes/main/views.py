from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(response):
    return render(response, "main.html")

@login_required(login_url="/signin")
def profile(response):
    arg = {"user": response.user}
    return render(response, "account.html", arg)

@login_required(login_url="/signin")
def dashboard(response):
    if response.user.is_staff:
        return render(response, "teacher.html")
    else:
        return render(response, "student.html")