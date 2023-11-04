from django.shortcuts import render

# Create your views here.
def login_fun(request):
    return render(request, 'login.html')


def register_fun(request):
    return render(request, 'register.html')