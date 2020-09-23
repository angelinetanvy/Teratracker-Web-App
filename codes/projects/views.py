from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def create_project(response):
    if response.method == 'POST':
        form = forms.CreateProjects(response.POST, response.FILES)
        if form.is_valid():
            # save project to db
            return redirect('/dashboard')
    else:
        form = forms.CreateProjects()
    ctx = {'form': form, 'FullName': response.user.get_full_name}
    return render(response, "create_project.html", ctx)
