from django.urls import path
from student.views import student_dasboard,edit_student,delete_student,student_logged_in,student_profile,student_him_self
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('student/',student_dasboard ,name='student'),
    path('logout/',LogoutView.as_view() ,name='logout'),
    path('student_logged_in/',student_logged_in ,name='student_logged_in'),
    path('student_him_self/<int:pk>/',student_him_self ,name='student_him_self'),
    path('student_profile/',student_profile ,name='student_profile'),
    path('edit_student/<int:pk>/',edit_student ,name='edit_student'),
    path('delete_student/<int:pk>/',delete_student ,name='delete_student'),
]