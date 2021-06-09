from django.shortcuts import render
from .models import Student, Teacher, Paper, Exam, Grade
from exam.models import Student, Teacher, Paper, Exam, Grade
from django.contrib.auth.decorators import login_required
from exam.models import models
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# questions = [
#     {
#         'question': '2 + 4',
#         'option1': '5',
#         'option2': '6',
#         'option3': '1',
#         'option4': '7',
#     },

#     {
#         'question': '2 + 3',
#         'option1': 'This is not a mathematical option',
#         'option2': '6',
#         'option3': '1',
#         'option4': '5',
#     },

#     {
#         'question': '10 * 3',
#         'option1': '110',
#         'option2': '30',
#         'option3': 'This is not a mathematical option',
#         'option4': '5',
#     }
# ]

# @login_required
def home(request):
    context = {
        'questions': Exam.objects.all()
    }
    return render(request, 'exam/home.html', context)


class ExamListView(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'exam/home.html'
    context_object_name = 'questions'


# class ExamCreateView(CreateView):
#     model = Exam
#     fields = '__all__'




def about(request):
    return render(request, 'exam/about.html')




# def student_login(request):
#     if request.method == 'POST':
#         stuid = request.POST.get('id')
#         password = request.POST.get('password')
#         print("id", stuid, "password", password)
#         student = models.Student.objects.get(id=stuid)
#         print(student)
#         if password == Student.password:
#             paper = models.Paper.objects.filter(major=Student.major)
#             grade = models.Grade.objects.filter(sid=Student.id)
#     # render index template
#             return render(request, 'students/demo.html', {'student': student, 'paper': paper, 'grade': grade})

#     else:
#         return render(request, 'students/demo.html', {'message': 'Incorrect password'})