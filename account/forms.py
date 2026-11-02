from django import forms
from account.models import Subject,Timetable,User


class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    comf_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','name','password','comf_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        comf_password = cleaned_data.get('comf_password')

        if password!=comf_password:
            self.add_error('comf_password','password and comfim password did not match')
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('user with this email alread exists')
        return email

class subjectform(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_code','subject_name','level','department','subject_type','periods_per_week','teacher_assigned','description']


class timetableform(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['class_name','day','start_time','end_time','subject','teacher','room']