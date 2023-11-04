from django.urls import path
from StudentApp import views


urlpatterns = [
    path('', views.login_fun, name='login'),
    path('reg', views.register_fun, name='reg'),
]