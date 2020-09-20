from django.urls import path

from . import views
from signin import views as signin_views

urlpatterns = [
    path("", views.index, name="index"),
    path("signin/", signin_views.signin, name="out")
]