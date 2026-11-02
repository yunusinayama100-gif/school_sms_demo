from django.contrib import admin
from account.models import Subject,Timetable,User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModelAdmin(UserAdmin):
    model = User
    list_display = ['id','email','name','is_active','is_student','is_teacher','is_staff','is_superuser','created_at','updated_at']

    list_filter = ['is_superuser']
    fieldsets = [('user credentail',{'fields':['email','password']}),('personal info',{'fields':['name']}),('permissions',{'fields':['is_active','is_staff','is_student','is_teacher','is_superuser']})]

    search_fields = ['email','name']
    ordering = ['email','id']
    filter_horizontal = []


admin.site.register(User,UserModelAdmin)



@admin.register(Subject)
class Subjectadmin(admin.ModelAdmin):
    list_display =('subject_code','subject_name','level','department','subject_type','periods_per_week','teacher_assigned','description')


@admin.register(Timetable)
class Timetableadmin(admin.ModelAdmin):
    list_display =('class_name','day','start_time','end_time','subject','teacher','room')