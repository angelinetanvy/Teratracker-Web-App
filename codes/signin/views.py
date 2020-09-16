from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
def signin(response):
    if response.method == "POST":
        form = AuthenticationForm(data=response.POST)
        if form.is_valid():
            user = form.get_user()
            login(response, user)
            return redirect("profile/")
    else:
        form = AuthenticationForm()
    return render(response, "signin.html", {"form": form})

def signout(response):
    if response.method == "POST":
        logout(response)
        return redirect("/out/")

def profile(response):
    arg = {"user": response.user}
    return render(response, "account.html", arg)