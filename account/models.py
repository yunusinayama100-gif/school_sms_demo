from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.utils import timezone

# Create your models here.
#customer user 

class UserManager(BaseUserManager):
    #create and save normal user and save to database
    def create_user(self,email,password=None):

        if not email:
            raise ValueError('user must have valid email address')
        User = self.model(email=self.normalize_email(email))
        User.set_password(password)
        User.save(using=self._db)
        return User

    #create superuser and save to database
    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must is_staff=true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must is_superuser=true.')

        #saving superuser with given email and password
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.is_student = True
        user.is_teacher = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    registration_number = models.CharField(max_length=20,unique=True,blank=True,null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.is_student and not self.registration_number:
            if self.pk is None:
                super().save(*args, **kwargs)

            year = timezone.localdate().year
            self.registration_number = (
                f"DIT-{year}-{self.pk:04d}"
            )

            return super().save(
                update_fields=["registration_number"]
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_superuser

    def has_module_perms(self,app_label):
        return self.is_superuser

    






class Subject(models.Model):
    subject_code = models.CharField(max_length=50)
    subject_name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    subject_type = models.CharField(max_length=50)
    periods_per_week = models.CharField(max_length=50)
    teacher_assigned = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.subject_name


class Timetable(models.Model):
    class_name = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    room = models.CharField(max_length=50)

    def __str__(self):
        return self.class_name