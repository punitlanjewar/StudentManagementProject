from StudentApp.models import Course
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

# Create your views here.
def login_fun(request):
    if request.method == 'POST':
        user_name = request.POST['txtName']
        user_password = request.POST['txtPassword']
        l1 = authenticate(username=user_name, password = user_password)
        if l1 is not None:
            if l1.is_superuser: # for checking superuser or not
                request.session['Uname'] = user_name
                return redirect('home')
        else:      
            return render(request, 'login.html', {'Msg': 'Username And Password is Incorrect'})
    else:
        return render(request, 'login.html')    


def register_fun(request):
    if request.method == 'POST': # this block for submit button
        user_name = request.POST['txtName']
        user_password = request.POST['txtPassword']
        user_email = request.POST['txtEmail']
        r1 = User.objects.create_superuser(username = user_name, password = user_password, email = user_email)
        r1.save()
        return redirect('login')
    else: # this block for hyperlink
        return render(request, 'register.html')
    

def home_fun(request):
    return render(request, 'home.html', {'Name': request.session['Uname']})


def addcourse_fun(request):
    if request.method == 'POST': 
        c1 = Course()
        c1.course_name = request.POST['txtCourseName']
        c1.course_duation = request.POST['txtCourseDuration']
        c1.course_fees = int(request.POST['txtCourseFees'])
        c1.save()
        return render(request, 'addcourse.html', {'Msg': 'Course Successfully Added'})
    else: # this block for hyperlink
        return render(request, 'addcourse.html')

