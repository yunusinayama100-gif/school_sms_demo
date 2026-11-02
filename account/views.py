from django.shortcuts import render,redirect,get_object_or_404
from account.forms import subjectform,timetableform
from django.contrib import messages
from account.models import Subject

# Create your views here.
def home(request):
    return render(request,'account/base.html')

def admin(request):
    return render(request,'account/admin.html')

def subjects(request):
    form = subjectform
    subjects_list = Subject.objects.all()
    if request.method == 'POST':
        subject_data = form(request.POST)
        if subject_data.is_valid():
            subject_data.save()
            messages.success(request,'subject successfully saved')
            return redirect('subjects')
        print(subject_data.errors)
        messages.error(request,'subject did not saved')
        return redirect('subjects')
    else:
        return render(request,'account/subjects.html',{'forms':form,'subjects':subjects_list})

def edit_subject(request,pk):
    if request.method == 'POST':
        subject_exist = get_object_or_404(Subject,pk=pk)
        editing_subject = subjectform(request.POST,instance=subject_exist)
        if editing_subject.is_valid():
            editing_subject.save()
            messages.success(request,'subject edited successfully')
            return redirect('subjects')
        messages.error(request,'subject did not edited')
        return redirect('subjects')
    else:
        return redirect('subjects')

def delete_subject(request,pk):
    if request.method == 'POST':
        subject_exist = get_object_or_404(Subject,pk=pk)
        if subject_exist:
            subject_exist.delete()
            messages.success(request,'subject deleted successfully')
            return redirect('subjects')
        messages.error(request,'subject did not deleted')
        return redirect('subjects')
    else:
        return redirect('subjects')
    

def timetables(request):
    if request.method == 'POST':
        form_data = timetableform(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'timetable added successfully')
            return redirect('timetables')
        messages.success(request,'timetable did not added')
        return redirect('timetables')
    else:
        form = timetableform
        return render(request,'account/timetable.html',{'form':form})