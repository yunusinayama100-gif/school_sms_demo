from django.urls import path
from account.views import home,admin,subjects,timetables,edit_subject,delete_subject
from account.authenticates import registration_page,login_page

urlpatterns = [
    path('registration_page/',registration_page,name='registration_page'),
    path('login_page/',login_page,name='login_page'),

    path('',home,name='students'),
    path('admin_page/',admin,name='admin_page'),
    path('subjects/',subjects,name='subjects'),
    path('edit_subject/<int:pk>/',edit_subject,name='edit_subject'),
    path('delete_subject/<int:pk>/',delete_subject,name='delete_subject'),
    path('timetables/',timetables,name='timetables'),
]