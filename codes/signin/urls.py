from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
    path('signin/', views.signout, name='signout'),
    path("profile/", views.profile, name="profile")
]
