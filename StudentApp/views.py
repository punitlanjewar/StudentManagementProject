from StudentApp.models import City, Course, Student
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
    if request.method == 'POST': # this block for button
        c1 = Course()
        c1.course_name = request.POST['txtCourseName']
        c1.course_duation = request.POST['txtCourseDuration']
        c1.course_fees = int(request.POST['txtCourseFees'])
        c1.save()
        return render(request, 'addcourse.html', {'Msg': 'Course Successfully Added'})
    else: # this block for hyperlink
        return render(request, 'addcourse.html')


def displaycourse_fun(request):
    course_data = Course.objects.all()
    return render(request, 'displaycourse.html', {'coursedata': course_data})


def update_fun(request, id):
    c1 = Course.objects.get(id=id)
    if request.method == 'POST': # block for button
        c1.course_name = request.POST['txtCourseName']
        c1.course_duation = request.POST['txtCourseDuration']
        c1.course_fees = int(request.POST['txtCourseFees'])
        c1.save()
        return render(request, 'updatecourse.html', {'Msg': 'Course Update Successfully'})
    else: # block for hyperlink
        return render(request, 'updatecourse.html', {'data': c1})
    

def deletecourse_fun(request, id):
    c1 = Course.objects.get(id=id)
    c1.delete()
    return redirect('displaycourse')


def addstudent_fun(request):
    if request.method == 'POST':
        s1 = Student()
        s1.stud_name = request.POST['txtStudentName']
        s1.stud_phno = int(request.POST['txtStudentPhone'])
        s1.stud_email = request.POST['txtStudentEmail']
        s1.stud_course = Course.objects.get(course_name=request.POST['selCourse'])
        s1.stud_city = City.objects.get(city_name=request.POST['selCity'])
        s1.paid_fees = int(request.POST['txtPaidFee'])
        c1 = Course.objects.get(course_name=request.POST['selCourse'])
        s1.pending_fees = c1.course_fees - s1.paid_fees
        s1.save()
        return render(request, 'addstudent.html', {'Msg': 'Student Data Successfully Added'})
    else:
        city = City.objects.all()
        course = Course.objects.all()
        return render(request, 'addstudent.html', {'CityData': city, 'CourseData': course})
    

def displaystudent_fun(request):
    stud_data = Student.objects.all()
    return render(request, 'displaystudent.html', {'StudentData': stud_data})
