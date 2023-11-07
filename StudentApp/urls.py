from django.urls import path
from StudentApp import views


urlpatterns = [
    path('', views.login_fun, name='login'), # redirect to login page
    path('reg', views.register_fun, name='reg'), # redirect to register page
    path('home', views.home_fun, name='home'), # redirect to home page
    path('add_course', views.addcourse_fun, name='add_course'), # redirect to course add page
    path('displaycourse', views.displaycourse_fun, name='displaycourse'), # it will collect data from database table and display into html page
    path('update/<int:id>', views.update_fun, name='update'), # it will redirect to update page
    path('delete/<int:id>', views.deletecourse_fun, name='delete'), # it will delete the (row) objects
    path('add_student', views.addstudent_fun, name='add_student'), # it will display addstudent pageand read and store into student table
    path('displaystudent', views.displaystudent_fun, name='displaystudent'), 
]