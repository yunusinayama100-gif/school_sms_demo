from django.contrib import admin
from teacher.models import Teacher,Work_detail

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','gender','date_of_birth','phone_number','email','photo','home_address','created_at',)

@admin.register(Work_detail)
class Work_detailAdmin(admin.ModelAdmin):
    list_display = ('id','teacher_id','employed_on','qualification','employment_type','subject_tought','class_assigned')