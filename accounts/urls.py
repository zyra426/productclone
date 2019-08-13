from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.signup, name="sign-up"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]