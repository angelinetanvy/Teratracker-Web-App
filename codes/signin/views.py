from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signin(response):
    if response.method == "POST":
        form = AuthenticationForm(data=response.POST)
        if form.is_valid():
            user = form.get_user()
            login(response, user)
            if "next" in response.POST:
                return redirect(response.POST.get('next'))
            return redirect("/dashboard")
    else:
        form = AuthenticationForm()
    return render(response, "signin.html", {"form": form})

def signout(response):
    logout(response)
    return redirect("/signin")

