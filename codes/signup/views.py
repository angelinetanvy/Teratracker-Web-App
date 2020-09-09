from django.shortcuts import render, redirect
from .forms import SignUpFormTerbul
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def signup(response):
    if response == "POST":
        form = SignUpFormTerbul(response.POST)
        # form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = SignUpFormTerbul()
        # form = UserCreationForm()
    return render(response, "signup/signup.html", {"form": form})
