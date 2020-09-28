from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext
from . import forms

# Create your views here.
def signin(response):
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
        context['signupFail'] = 'false'
    return render(response, "signin.html", context)

def signout(response):
    logout(response)
    return redirect("/signin")

