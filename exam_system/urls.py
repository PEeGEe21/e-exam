"""exam_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from lecturers import views as lecturer_views
from django.conf import settings

from students import views as student_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('exam.urls')),
    path('students/', student_views.dashboard, name='students_dashboard'),
    path('video/', student_views.video, name='videocam'),
    # url(r'^studentLogin/$', student_views.studentLogin, name='studentslogin'),
    url(r'^studentLogin/startexam/$', student_views.studentLogin, name='studentslogin'),
 
    # url(r'^studentLogin/startexam/$', student_views.startExam, name='startexam'),
    # path('studentLogin/', auth_views.LoginView.as_view(template_name='students/login.html'), name='studentlogin'),
    path('student/logout/', auth_views.LogoutView.as_view(template_name='students/logout.html'), name='logout'),
    path('student/login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='students-login'),

    # path('', student_views.login, name='students-login'),
    path('signup/', student_views.register, name='students-register'),
    # path('result/', student_views.result, name='student-result'),
    url(r'^result/$',student_views.calGrade),
    url(r'^face_detection/detect/$',student_views.detect),
    url('queryStudent',student_views.queryStudent, name='querystudent'),
    # url(r'^studentLogin/exam/', include('exam.urls')),
    path('lecturer/', include('lecturers.urls')),
    url(r'^examination/', student_views.examstart, name='examination' ),

]


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)