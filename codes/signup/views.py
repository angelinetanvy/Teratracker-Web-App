from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def signup(response):
    if response.method == "POST":
        form = forms.SignUpForm(data = response.POST)
        # form = forms.testForm(data = response.POST)
        if form.is_valid():
            form.save()
            return redirect("/signin/")
    else:
        form = forms.SignUpForm()
        # form = forms.testForm()
    return render(response, "signup.html", {"form": form})