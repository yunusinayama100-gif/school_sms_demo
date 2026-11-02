from django.db import models
from account.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,choices=[('Male','Male'),('Female','Female')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    admission_date = models.DateField()
    photo = models.ImageField(upload_to='images')
    home_address = models.TextField()
    blood_group = models.CharField(max_length=50)
    allergies = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class parent(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name


