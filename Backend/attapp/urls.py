from django.urls import path
from . import views

urlpatterns = [
    path('api/teacher/register/', views.teacher_register, name='teacher_register'),
    path('api/student/register/', views.student_register, name='student_register'),
    path('api/teacher/login/', views.teacher_login, name='teacher_login'),
    path('api/student/login/', views.student_login, name='student_login'),
    path('api/save_attendance/', views.save_attendance, name='save_attendance'),
]
