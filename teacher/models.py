from django.db import models

# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50,choices=[('Male','Male'),('Female','Female')])
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    photo = models.ImageField(upload_to='teacher_images')
    home_address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Work_detail(models.Model):
    teacher_name = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=50)
    employed_on = models.DateField()
    qualification = models.CharField(max_length=50)
    employment_type = models.CharField(max_length=50)
    subject_tought = models.CharField(max_length=50)
    class_assigned =  models.CharField(max_length=50)
    def __str__(self):
        return str(self.teacher_id )   