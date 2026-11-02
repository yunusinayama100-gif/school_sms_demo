from django.urls import path
from teacher.views import teacher_dashboard,add_teacher,edit_teacher,delete_teacher,teacher_logged_in,teacher_profile

urlpatterns = [
    path('teacher_dashboard/',teacher_dashboard,name='teacher_dashboard'),
    path('teacher_logged_in/',teacher_logged_in,name='teacher_logged_in'),
    path('teacher_profile/',teacher_profile,name='teacher_profile'),
    path('add_teacher/',add_teacher,name='add_teacher'),
    path('edit_teacher/<int:pk>/',edit_teacher,name='edit_teacher'),
    path('delete_teacher/<int:pk>/',delete_teacher,name='delete_teacher'),
]