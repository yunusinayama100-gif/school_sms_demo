from django.shortcuts import render,redirect,get_object_or_404
from teacher.forms import TeaacherForm,WorkDetailsForm
from teacher.models import Teacher,Work_detail
from django.db import transaction
from django.contrib import messages

# Create your views here.
def teacher_logged_in(request):
    return render(request,'teacher/teacher_logged_in.html')

def teacher_profile(request):
    return render(request,'teacher/teacher_profile.html')


def teacher_dashboard(request):
    teacher_list = Teacher.objects.all()
    teacher =TeaacherForm()
    work = WorkDetailsForm()
    return render(request,'teacher/teacher_dashboard.html',{'teacher':teacher,'work':work,'teachers':teacher_list})

def add_teacher(request):
    if request.method == 'POST':
        teacher_info = TeaacherForm(request.POST,request.FILES)
        workdetail_info = WorkDetailsForm(request.POST)
        if teacher_info.is_valid() and workdetail_info.is_valid():
            with transaction.atomic():
                teacher_obj = teacher_info.save()
                #saving parent with instance of student
                workdetail_obj = workdetail_info.save(commit=False)
                workdetail_obj.teacher_name = teacher_obj
                workdetail_obj.save()

                messages.success(request,'teacher data succesffully saved')
                return redirect('teacher_dashboard')
        messages.error(request,'teacher did not saved')
        return redirect('teacher_dashboard')
    else:
        return redirect('teacher_dashboard')


def edit_teacher(request,pk):
    if request.method=='POST':
        teacher_exist = get_object_or_404(Teacher,pk=pk)
        workdetails_exist = get_object_or_404(Work_detail,teacher_name=teacher_exist)
        teacher_edit = TeaacherForm(request.POST,request.FILES,instance=teacher_exist)
        workdetails_edit = WorkDetailsForm(request.POST,instance=workdetails_exist)
        if teacher_edit.is_valid() and workdetails_edit.is_valid():
            with transaction.atomic():
                teacher_obj = teacher_edit.save()
                workdetails_obj = workdetails_edit.save(commit=False)
                workdetails_obj.teacher_name = teacher_obj
                workdetails_obj.save()
                messages.success(request,'teacher edited successfully')
                return redirect('teacher_dashboard')
        messages.error(request,'teacher did not edited')
        print(teacher_edit.errors)
        return redirect('teacher_dashboard')
    else:
        return redirect('teacher_dashboard')


def delete_teacher(request,pk):
    if request.method=='POST':
        teacher_exist = Teacher.objects.get(pk=pk)
        if teacher_exist:
            teacher_exist.delete()
            messages.success(request,'teacher deleted successfully')
            return redirect('teacher_dashboard')
        messages.error(request,'teacher did not deleted there is miss much of information')
        return redirect('teacher_dashboard')
    else:
        return redirect('teacher_dashboard')
   