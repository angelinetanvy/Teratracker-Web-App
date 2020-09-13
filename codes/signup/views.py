from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def signup(response):
    if response.method == "POST":
        form = forms.SignUpForm(data = response.POST)
        # form = UserCreationForm(data = response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect("/signin/")
    else:
        form = forms.SignUpForm()
        # form = UserCreationForm()
    return render(response, "signup/signup.html", {"form": form})
