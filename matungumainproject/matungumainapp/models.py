from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    object = models.manager
    department_Code = models.CharField(max_length=40)
    department_Name = models.CharField(max_length=40)

    def __str__(self):
        return f'Department({self.department_Name})'


class Members(models.Model):
    # administrator = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=30, null=True, blank=True, unique=True)
    # gender = models.CharField(max_length=7, null=True, blank=True, choices=gender_category)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    # profile_pic = models.ImageField(default="patient.jpg", null=True, blank=True)
    age = models.IntegerField(default='0', blank=True, null=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    date_entered = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'Member({self.first_name},  {self.last_name})'



