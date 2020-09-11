from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def signin(response):
    if response == "POST":
        form = AuthenticationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthenticationForm()
    return render(response, "signin/signin.html", {"form": form})
