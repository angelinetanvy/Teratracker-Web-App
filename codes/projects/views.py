from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from . import forms
from .models import Project, ProjectStudents, Task, TaskStudents
from django.contrib.auth.models import User


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
        projects = []
        projectStudents = ProjectStudents.objects.filter(student=response.user)
        if len(projectStudents) > 0:
            for item in projectStudents:
                projects.append(item.project)
        projects.sort(key=lambda project: project.due_date)
        template = "studentdashboard.html"

    arg = {"FirstName": response.user.first_name.capitalize,
           "FullName": response.user.get_full_name,
           "Projects": projects}
    return render(response, template, arg)


@login_required(login_url="/signin")
def project_info(response, project):
    students = []
    project = Project.objects.filter(title=project)[0]
    projectStudents = ProjectStudents.objects.filter(project=project)

    task = display_task(project.id)

    if response.user.is_staff:
        AccountType = "Teacher"
    else:
        AccountType = "Student"

    if len(projectStudents) > 0:
        for i in projectStudents:
            students.append(i.student.first_name + " " + i.student.last_name)

    arg = {"FirstName": response.user.first_name.capitalize,
           "FullName": response.user.get_full_name,
           "Project": project,
           "Students": students,
           "AccountType": AccountType,
           "Task": task
           }
    response.session['project_id'] = project.title
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


@login_required(login_url="/signin")
def create_task(response):
    project_id = response.session["project_id"]
    if response.method == 'POST':
        form = forms.CreateTask(response.POST, response.FILES)
        form.specify(project_id)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/project-info/' + project_id + '/')
    else:
        form = forms.CreateTask()
        form.specify(project_id)
    arg = {"form": form}

    return render(response, "create_task.html", arg)


def display_task(project_id):
    task_display = []
    task = Task.objects.filter(sourceproject=project_id)

    for t in task:
        task_display.append(t.taskname)

    return task_display


@login_required(login_url="/signin")
def task_info(response, task):
    members = []
    prop = []
    task = Task.objects.filter(taskname=task)[0]

    task_members = TaskStudents.objects.filter(task_id=task.id).values_list('student_id')
    task_time = TaskStudents.objects.filter(task_id=task.id).values_list('time', flat=True)
    total_tasktime = 0

    for i in range(len(task_time)):
        total_tasktime += int(str(task_time[i]))

    for i in range(len(task_members)):
        memberProportion = round(int(str(task_time[i])) / total_tasktime * 100, 2)
        prop.append(memberProportion)
        members.append(str(User.objects.get(id=task_members[i][0])) + " (" + str(task_time[i]) + " hours) (" + str(memberProportion) + "%)")

    data = zip(members, prop)
    arg = {
        "Task": task,
        "Size": range(len(task_members)),
        "Data": data
    }
    response.session['project_id'] = str(task.sourceproject)
    response.session['task'] = task.id
    return render(response, 'TaskInfo.html', arg)


@login_required(login_url="/signin")
def assign_members(response):
    project_id = response.session["project_id"]
    task_id = response.session["task"]
    if response.method == 'POST':
        form = forms.AssignMembers(response.POST, response.FILES, user=response.user)
        form.specify(task_id, project_id)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/assign-members")
    else:
        form = forms.AssignMembers(user=response.user)
        form.specify(task_id, project_id)
    arg = {"FullName": response.user.get_full_name, "form": form}
    return render(response, "assign_members.html", arg)
