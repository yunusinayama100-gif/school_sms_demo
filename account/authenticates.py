from django.shortcuts import render,redirect
from account.forms import Userform
from django.contrib import messages
from account.models import User
from django.contrib.auth import authenticate,login

def registration_page(request):
    if request.method == 'POST':
        User_data = Userform(request.POST)
        if User_data.is_valid():
            User = User_data.save(commit=False)
            User.set_password(User_data.cleaned_data['password'])
            User.is_active= False
            User.save()
            messages.success(request,'registration completed seccessfully check activation link to your registered email to activate acount')
            return redirect('login_page')
        
        messages.error(request,User_data.errors)
        return redirect('registration_page')
    else:
        form = Userform
        return render(request,'account/authenticate/registration.html',{'form':form})

def login_page(request):   
    if request.user.is_authenticated:
        if request.user.is_student:
            return redirect('student_logged_in')
        elif request.user.is_teacher:
            return redirect('teacher_logged_in')
        elif request.user.is_staff:
            return redirect('admin_page')
        else:
            messages.error(request,'the system can identifing you please contact to administrator')
            return redirect('login_page')

    if request.method=='POST':
        email  = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request,'Both field are requred')
            return redirect('login_page')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request,'Invalid email or password')
            return redirect('login_page')
        
        if not user.is_active:
            messages.error(request,'user not active please activate your account via activation link sent to registerd email')
            return redirect('login_page') 
        
        #checking the user having email and password give if present
        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'your successfully logged thanks')
            if user.is_student:
                return redirect('student_logged_in')
            elif user.is_teacher:
                return redirect('teacher_logged_in')
            elif user.is_staff:
                return redirect('admin_page')
            else:
                messages.error(request,'You do not have permission to asses this area')
                return redirect('login_page')  
        else:
            messages.error(request,'Invalid email or password')
            return redirect('login_page')
    else:
        return render(request,'account/authenticate/login.html')