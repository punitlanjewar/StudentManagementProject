from django.urls import path
from StudentApp import views


urlpatterns = [
    path('', views.login_fun, name='login'), # redirect to login page
    path('reg', views.register_fun, name='reg'), # redirect to register page
    path('home', views.home_fun, name='home'), # redirect to home page
    path('add_course', views.addcourse_fun, name='add_course'), # redirect to course add page
    
]