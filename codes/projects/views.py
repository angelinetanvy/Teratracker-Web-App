from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from . import forms
from .models import Project, ProjectStudents

# Create your views here.
@login_required(login_url="/signin")
def create_project(response):
    if response.user.is_staff:
        if response.method == 'POST':
            form = forms.CreateProjects(response.POST, response.FILES)
            if form.is_valid():
                # save project to db
                # form.save()
                try:
                    instance = form.save(commit=False)
                    instance.supervisor = response.user
                    instance.save()
                except IntegrityError:
                    ctx = {'form': form, 'FullName': response.user.get_full_name,
                           'err': 'Project Title Already Exists'}
                    return render(response, "create_project.html", ctx)

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
    if response.user.is_staff:
        projects = Project.objects.filter(supervisor=response.user).order_by('due_date')
        template = "teacherdashboard.html"
    else:
        projects = Project.objects.all().order_by('due_date')   # Filter need to be applied here
        template = "studentdashboard.html"

    arg = {"FirstName": response.user.first_name.capitalize,
           "FullName": response.user.get_full_name,
           "Projects": projects}
    return render(response, template, arg)

@login_required(login_url="/signin")
def project_info(response,project):
    students = []
    project = Project.objects.filter(title=project)[0]
    projectStudents = ProjectStudents.objects.filter(project=project)
    if (len(projectStudents)>0):
        for i in projectStudents:
            students.append(i.student.first_name+" "+i.student.last_name) 

    arg = {"FirstName": response.user.first_name.capitalize,
           "FullName": response.user.get_full_name,
           "Project" : project,
           "Students": students
          }
    return render(response, "ProjectInfo.html", arg)

@login_required(login_url="/signin")
def assign_students(response):
    if response.method == 'POST':
        form = forms.AssignStudents(response.POST, response.FILES, user=response.user)

        if form.is_valid():
            form.save()
            return redirect("/dashboard/assign-students")
    else:
        form = forms.AssignStudents(user=response.user)
    ctx = {"FullName": response.user.get_full_name, "form": form}
    return render(response, "assignstudents.html", ctx)
