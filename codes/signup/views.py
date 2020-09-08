from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(response):
    if response.method == "POST":
=======
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(response):
    if response == "POST":
>>>>>>> Shane
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
<<<<<<< HEAD
    return render(response, "SignUpPage/SignUpPage.html", {"form": form})
=======
    return render(response, "signup/signup.html", {"form": form})
>>>>>>> Shane
