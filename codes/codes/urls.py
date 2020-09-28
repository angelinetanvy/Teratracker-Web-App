"""codes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from main import views as main_views
from signin import views as signin_views
from signup import views as signup_views
from projects import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name="index"),
    path('signup/', signup_views.signup, name='signup'),
    path('signin/', signin_views.signin, name='signin'),
    path('signout/', signin_views.signout, name='signout'),
    path('dashboard/', project_views.dashboard, name='dashboard'),
    path('profile/', main_views.profile, name='profile'),
    
    path('dashboard/create-project/', project_views.create_project, name='create-project'),
    path('dashboard/project-info/<int:project>/', project_views.project_info, name='project-info'),
    path('dashboard/assign-students/', project_views.assign_students, name='assign-students'),

    path('dashboard/create-task/', project_views.create_task, name='create-task'),
    path('dashboard/task-info/<int:task>/', project_views.task_info, name='task-info'),
    path('dashboard/task-info/<int:task>/confirmation/', project_views.close_task, name='confirmation'),
    path('dashboard/assign-members/', project_views.assign_members, name='assign-members'),
    
    path('', include("django.contrib.auth.urls"))
]
