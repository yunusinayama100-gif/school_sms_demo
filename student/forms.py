from django import forms
from student.models import Student,parent

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','gender','date_of_birth','student_class','section','admission_date','photo','home_address','blood_group','allergies',]


class parentform(forms.ModelForm):
    class Meta:
        model = parent
        fields = ['full_name','relationship','phone_number','email',]