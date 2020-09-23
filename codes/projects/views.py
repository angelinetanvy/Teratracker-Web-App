from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Project

# Create your views here.
@login_required(login_url="/signin")
def create_project(response):
    if response.user.is_staff:
        if response.method == 'POST':
            form = forms.CreateProjects(response.POST, response.FILES)
            if form.is_valid():
                # save project to db
                instance = form.save(commit=False)
                instance.supervisor = response.user
                instance.save()
                return redirect('/dashboard')
        else:
            form = forms.CreateProjects()
        ctx = {'form': form, 'FullName': response.user.get_full_name}
    else:
        form = "Only Teachers can create projects"
        ctx = {'form': form, 'FullName': response.user.get_full_name}
    return render(response, "create_project.html", ctx)

@login_required(login_url="/signin")
def dashboard(response):
    first_name = response.user.first_name.capitalize
    full_name = response.user.get_full_name
    projects = Project.objects.all().order_by('due_date')

    if response.user.is_staff:
        UserType, Authorization = "Teacher", "true"
    else:
        UserType, Authorization = "Student", "false"

    arg = {"UserType": UserType,
           "FirstName": first_name,
           "FullName": full_name,
           "Projects": projects,
           "Authorized": Authorization}

    return render(response, "dashboard.html", arg)
