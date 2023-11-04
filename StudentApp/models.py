from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_duation = models.CharField(max_length=150)
    course_fees = models.IntegerField()


class City(models.Model):
    city_name = models.CharField(max_length=150)


class Student(models.Model):
    stud_name = models.CharField(max_length=150)
    stud_phno = models.BigIntegerField()
    stud_email = models.CharField(max_length=150)
    paid_fees = models.IntegerField()
    pending_fees = models.IntegerField()
    stud_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_city = models.ForeignKey(City, on_delete=models.CASCADE)       