from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(response):
    return redirect("/dashboard")


@login_required(login_url="/signin")
def profile(response):
    first_name = response.user.first_name.capitalize
    full_name = response.user.get_full_name
    if response.user.is_staff:
        user_type = "Teacher"
    else:
        user_type = "Student"
    arg = {"user": response.user, "UserType": user_type, "FirstName": first_name, "FullName": full_name}
    return render(response, "account.html", arg)

