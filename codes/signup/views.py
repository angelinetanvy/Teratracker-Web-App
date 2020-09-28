from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def signup(response):
    context = {}
    if response.method == "POST":
        signinform = forms.SignInForm(data=response.POST)
        signupform = forms.SignUpForm(data=response.POST)

        if signinform.is_valid():
            user = signinform.get_user()
            login(response, user)
            if "next" in response.POST:
                return redirect(response.POST.get('next'))
            return redirect("/dashboard")
        else:
            context['signinform'] = signinform

        if signupform.is_valid():
            signupform.save()
            context['signupform'] = signupform
            context['signupFail'] = 'false'
        else:
            context['signupform'] = signupform
            context['signupFail'] = 'true'
    else:
        context['signinform'] = forms.SignInForm()
        context['signupform'] = forms.SignUpForm()
        context['signupFail'] = 'true'
    return render(response, "signin.html", context)
