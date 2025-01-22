from django.urls import path
from . import views

urlpatterns=[
    path('/teacher/login',views.teacher_login,name='teacher_login'),
    path('/student/login',views.student_login,name='student_login'),
    path('/parent/login',views.parent_login,name='parent_login'),
]

