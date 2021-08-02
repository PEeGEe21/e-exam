from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
# from .views import ExamDeleteView


urlpatterns = [

    # # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
    path('logout/', auth_views.LogoutView.as_view(template_name='lecturers/logout.html'), name='lecturer_logout'),
    path('register/', views.register, name='lecturer_register'),
    path('question-list/', views.questionList, name='question_list'),
    path('student-report/', views.studentReport, name='student_report'),
    path('monitor-exam/', views.monitorExam, name='monitor_exam'),
    path('student-list/', views.studentList, name='student_list'),
    path('setup-exam/', views.ExamSetupView.as_view(), name='exam_setup'),
    # path('login/', views.login, name='lecturer-login'),
    path('login/', auth_views.LoginView.as_view(template_name='lecturers/login.html'), name='lecturer-login'),
    url(r'^teacherLogin/', views.teacherLogin, name='teacherLogin'),
    # url(r'^report/', views.report, name='report'),
    path('create/', views.ExamCreateView.as_view(), name='exam-create'),
    path('profile/', views.profile, name='lecturer-profile'),
    path('setting/', views.CoursecreateView.as_view(), name='lecturer-setting'),
    # path('exam/<id>/delete/', views.exam_delete_view, name='exam-delete'),
    # path('exam/<int:pk>/delete/', ExamDeleteView.as_view(template_name='lecturers/question_confirm_delete.html'), name='exam-delete'),

    # path('dashboard/', views.dashboard.as_view(template_name='lecturers/dashboard.html'), name='lecturer_dashboard'),
    path('dashboard/', views.dashboard, name='lecturer_dashboard'),
]