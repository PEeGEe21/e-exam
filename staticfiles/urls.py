from django.urls import path
from . import views


urlpatterns = [

    # path('home', views.home, name='exam-home'),
    path('home', views.ExamListView.as_view(), name='exam-home'),
    # path('create/', views.ExamCreateView.as_view(), name='exam-create'),

    path('about/', views.about, name='exam-about'),
    # path('login/', views.student_login, name='student-login'),
]