from django.shortcuts import render,redirect,get_object_or_404
from student.forms import studentform,parentform
from django.contrib import messages
from student.models import parent,Student
from django.db import transaction
from account.models import User

# Create your views here.
def student_logged_in(request):
    return render(request,'student/student_logged_in.html')

def student_profile(request):
    studentforms = studentform()
    parentforms = parentform()
    return render(request,'student/student_profile.html',{'student':studentforms,'parent':parentforms})


def student_dasboard(request):
    if request.method == 'POST':
        student_info = studentform(request.POST,request.FILES)
        parent_info = parentform(request.POST)
        if student_info.is_valid() and parent_info.is_valid():
            #saving student
            with transaction.atomic():
                student_obj = student_info.save()
                #saving parent with instance of student
                parent_obj = parent_info.save(commit=False)
                parent_obj.student = student_obj
                parent_obj.save()

                messages.success(request,'student data succesffully saved')
                return render(request,'student/student_dashboard.html')
        messages.success(request,'student data did not saved')
        return render(request,'student/student_dashboard.html')
    else:
        studentforms = studentform()
        parentforms = parentform()
        student_list = Student.objects.all()
        return render(request,'student/student_dashboard.html',{'student':studentforms,'parent':parentforms,'student_list':student_list})

def edit_student(request,pk):
    if request.method == 'POST':
        student_exist = get_object_or_404(Student,pk=pk)
        parent_exist = get_object_or_404(parent,student= student_exist)

        student_info = studentform(request.POST,request.FILES,instance=student_exist)
        parent_info = parentform(request.POST,instance=parent_exist)

        if student_info.is_valid() and parent_info.is_valid():
            with transaction.atomic():
                student_obj = student_info.save()
                #saving parent with instance of student
                parent_obj = parent_info.save(commit=False)
                parent_obj.student = student_obj
                parent_obj.save()

                messages.success(request,'student edited succesffully')
                return redirect('student')
        messages.success(request,'student data did not edited')
        return redirect('student')
    else:
        return redirect('student')


def delete_student(request,pk):
    if request.method == 'POST':
        student_exist = get_object_or_404(Student,pk=pk)
        if student_exist:
            student_exist.delete()
            messages.success(request,'student deleted successuflly')
            return redirect('student')
        messages.success(request,'student did not deleted')
        return redirect('student')
    else:
        return redirect('student')



def student_him_self(request,pk):
    if request.method == 'POST':
        student_info = studentform(request.POST,request.FILES)
        if student_info.is_valid():
            existing_user = get_object_or_404(User,pk=pk)
            student_obj = student_info.save(commit=False)
            #saving parent with instance of student
            student_obj.user = existing_user
            student_obj.save()
            #saving student
            messages.success(request,'student data succesffully saved')
            return redirect('student_profile')
        print(student_info.errors)
        messages.success(request,'student data did not saved')
        return redirect('student_profile')
    else:
        return redirect('student_profile')