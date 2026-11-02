from django.contrib import admin
from student.models import Student,parent

# Register your models here.
@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','gender','date_of_birth','student_class','section','admission_date','photo','home_address','blood_group','allergies',)

@admin.register(parent)
class parentsAdmin(admin.ModelAdmin):
    list_display = ('id','student','full_name','relationship','phone_number','email',)