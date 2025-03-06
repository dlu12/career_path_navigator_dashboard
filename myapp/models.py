from django.db import models

# Create your models here.
from django.db.models import Model
from django.shortcuts import render

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class Company(models.Model):
    name = models.CharField(max_length=100)
    since = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    logo = models.CharField(max_length=300)
    photo = models.CharField(max_length=300)
    proof = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Skill(models.Model):
    skillname = models.CharField(max_length=100)

class College(models.Model):
    name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    photo = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    since = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)

class Vaccancy(models.Model):
    vaccancy_no = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    experience = models.CharField(max_length=100)
    COMPANY = models.ForeignKey(Company, on_delete=models.CASCADE)


class Notification(models.Model):
    date = models.DateField()
    notification = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)
    qualification = models.CharField(max_length=300)
    experience = models.CharField(max_length=300)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Complaint(models.Model):
    date = models.DateField()
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    COLLEGE=models.ForeignKey(College,on_delete=models.CASCADE,default="")

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    DEPARTMENT = models.ForeignKey(Department, on_delete=models.CASCADE)


class Vaccancy_Request(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    VACANCY = models.ForeignKey(Vaccancy, on_delete=models.CASCADE)


class OwnSkill(models.Model):
    SKILL = models.ForeignKey(Skill, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class FeeStruct(models.Model):
    fees = models.CharField(max_length=100)
    sem = models.CharField(max_length=100)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE)


class Facilities(models.Model):
    facility_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    photo = models.CharField(max_length=400)

class Resume(models.Model):
    resume = models.CharField(max_length=100)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Vaccancy_Skill(models.Model):
    VACCANCY = models.ForeignKey(Vaccancy, on_delete=models.CASCADE)
    SKILL = models.ForeignKey(Skill, on_delete=models.CASCADE)

class JobRequest(models.Model):
    date = models.DateField()
    USER =  models.ForeignKey(User, on_delete=models.CASCADE)
    VACANCY =models.ForeignKey(Vaccancy, on_delete=models.CASCADE)
    file=models.CharField(max_length=250)
    status=models.CharField(max_length=100)
