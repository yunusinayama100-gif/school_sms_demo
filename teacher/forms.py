from django import forms
from teacher.models import Teacher,Work_detail

class TeaacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name','gender','date_of_birth','phone_number','email','photo','home_address']


class WorkDetailsForm(forms.ModelForm):
    class Meta:
        model = Work_detail
        fields = ['teacher_id','employed_on','qualification','employment_type','subject_tought','class_assigned']

