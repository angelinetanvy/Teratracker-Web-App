from django.shortcuts import render, redirect
from .forms import SignUpForm
# Create your views here.
def signup(response):
    if response == "POST":
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = SignUpForm()
    return render(response, "signup/signup.html", {"form": form})
