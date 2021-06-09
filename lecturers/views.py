from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string

from django.urls import reverse
from django.http import HttpResponse
from exam.models import models
from .forms import ExamCreateForm
from .forms import ExamSetupForm
from .forms import ExamListForm
from .forms import StudentListForm
from .forms import StudentReportForm
import sweetify
from sweetify.views import SweetifySuccessMixin
from django.db import models
from django.views.generic import ListView, CreateView
from exam.models import Student, Paper, Teacher, Exam, Grade
from django.contrib.auth.decorators import login_required
# Import ListView module
from .forms import TeacherUpdateForm, ProfileUpdateForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Import Q module
from django.db.models import Q

from django.template import loader
from django import template
# from django.contrib.auth.forms import UserCreationForm
from .forms import TeacherRegisterForm
from django.contrib import messages
# from django.contrib.auth import login, authenticate



# @login_required(login_url="/lecturer/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
        
#         load_template      = request.path.split('/')[-1]
#         context['segment'] = load_template
        
#         html_template = loader.get_template( load_template )
#         return HttpResponse(html_template.render(context, request))
        
#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template( '/lecturers/page-404.html' )
#         return HttpResponse(html_template.render(context, request))

    # except:
    
    #     html_template = loader.get_template( '/lecturers/page-500.html' )
    #     return HttpResponse(html_template.render(context, request))




def examSetup(request):
    return render(request, 'lecturers/exam_setup.html')


      
def questionList(request):
        username = request.session['username']
        print("username::::::", username)

        teacher = Teacher.objects.get(username=username)
        print("teacher::::::", teacher)
        if request.method=='POST':
            form = ExamListForm(request.POST)
            

            if form.is_valid():

                subject1 = request.POST.get('course')
        
                context = {
                    'form': form,
                    'teacher': teacher,
                    # 'questions': Exam.objects.all(),
                    'course': form.cleaned_data.get('course'),
                    'questions': Exam.objects.filter(course=subject1),
                }
                print("subject1", subject1)
                return render(request,'lecturers/question_list.html', context)
        else: 
            context = {
                'form' : ExamListForm(),
                'teacher': teacher,
            }
            return render (request, 'lecturers/question_list.html', context)

# def studentList(request):
#     username = request.session['username']
#     teacher = Teacher.objects.get(username=username)
#     print("teacher.dept", teacher)
#     queryset = Student.objects.filter(dept=teacher.dept)
#     print("queryset", queryset)
#     if request.GET.keys():
#         if request.GET.get('src') != '':
#             keyword = request.GET.get('src')
#             queryset = Student.objects.filter(Q(brand=keyword.capitalize()) | Q(type=keyword.capitalize()))
#     context = {
#         'teacher': teacher,
#         'queryset': queryset
#     }
#     return render(request, 'lecturers/student_list.html', context)


def studentReport(request):
        username = request.session['username']
        print("username::::::", username)

        teacher = Teacher.objects.get(username=username)
        print("teacher::::::", teacher)
        if request.method=='POST':
            form = StudentReportForm(request.POST)
            
        
            if form.is_valid():

                subject = request.POST.get('course')
                lecturer = Paper.objects.get(course=subject)
                # print(lecturer.tid)
                grade = Grade.objects.filter(subject=subject)
                queryset = Grade.objects.filter(subject=subject)
                print("queryset", queryset)
                if request.GET.keys():
                    if request.GET.get('src') != '':
                        keyword = request.GET.get('src')
                        queryset = Paper.objects.filter(Q(brand=keyword.capitalize()) | Q(type=keyword.capitalize()))
                context = {
                    'form': form,
                    'teacher': teacher,
                    'lecturer': lecturer,
                    # 'questions': Exam.objects.all(),
                    'course': form.cleaned_data.get('course'),
                    'grade': grade,
                    'queryset': queryset,
                }
                print("subject", subject)
                print("grade", grade)
                return render(request,'lecturers/student_report.html', context)
        else: 
            context = {
                'form' : StudentReportForm(),
                'teacher': teacher,
            }
            return render (request, 'lecturers/student_report.html', context)




def register(request):
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        # username: ''
        if form.is_valid():
            form.save()
            username: form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            # return render(request, 'lecturers/login.html')
            return redirect('lecturer-login')
    else:
        form = TeacherRegisterForm()
    return render(request, 'lecturers/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = TeacherRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             name: form.cleaned_data.get('name')
#             username: form.cleaned_data.get('username')
#             sex: form.cleaned_data.get('sex')
#             dept: form.cleaned_data.get('dept')
#             email: form.cleaned_data.get('email')
#             birth: form.cleaned_data.get('birth')
#             # password: form.cleaned_data.get('password1')
#             user = authenticate(name=name, username=username,  sex=sex, dept=dept, email=email, birth=birth)
#             messages.success(request, f'Account Created for {username}!')
#             login(request, user)
#         return render(request, 'lecturers/dashboard.html')
#     else:
#         form = TeacherRegisterForm()
#         return render(request, 'lecturers/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = TeacherRegisterForm(request.POST)
#         form.save()

#         # if form.is_valid():
#         #     form.save()
#         #     username = form.cleaned_data.get('username')
#         #     messages.success(request, f'Account Created for {username}!')
#         #     return redirect('exam-home')
#         return render(request, 'lecturers/register.html')
#     else:
#         # form = TeacherRegisterForm()
        
#         return render(request, 'lecturers/dashboard.html')
#     # return render(request, 'lecturers/register.html', {'form': form})

# def dashboard(request):
    
#     username = request.session['username']
#     teacher = Student.objects.get(username=username)
#     print("teacher", teacher)
#     context = {
#         'teacher' : teacher
#     }
#     return render(request, 'lecturers/dashboard.html', context)


# Define class for Querying data
# class dashboard(ListView):
#     # Define model
#     model = Student
#     # Define template
#     template_name = 'lecturers/dashboard.html'
#     # context_object_name = 'teacher'


#     def get_queryset(self):
#         # Set the default query set
#         queryset = Student.objects.all()
#         # Check the form value is submitted or not
#         if self.request.GET.keys():
#             # Check the search keyword
#             if self.request.GET.get('src') != '':
#                 keyword = self.request.GET.get('src')
#                 # Set the query set based on search keyword
#                 queryset = Student.objects.filter(Q(brand=keyword.capitalize()) | Q(type=keyword.capitalize()))
#         return queryset


def dashboard(request):
    username = request.session['username']
    print("username::::::", username)
    teacher = Teacher.objects.get(username=username)
    print("teacher::::::", teacher)
    context = {
        'teacher': teacher,
    }
    return render(request, 'lecturers/dashboard.html', context)


def setting(request):
    username = request.session['username']
    print("username::::::", username)

    teacher = Teacher.objects.get(username=username)
    print("teacher::::::", teacher)
    context = {
        'teacher': teacher,
    }
    return render(request, 'lecturers/setting.html', context)

def studentList(request):
    username = request.session['username']
    teacher = Teacher.objects.get(username=username)
    print("teacher.dept", teacher)

    
    queryset = Student.objects.filter(dept=teacher.dept)
    print("queryset", queryset)
    # Check the form value is submitted or not
    if request.GET.keys():
        # Check the search keyword
        if request.GET.get('src') != '':
            keyword = request.GET.get('src')
            # Set the query set based on search keyword
            queryset = Student.objects.filter(Q(brand=keyword.capitalize()) | Q(type=keyword.capitalize()))

    context = {
        'teacher': teacher,
        'queryset': queryset
    }
    # if request.method=='POST':
        # form = StudentListForm(request.POST)
        

        # if form.is_valid():

    #         department = request.POST.get('student')
    
    #         context = {
    #             'form': form,
    #             # 'teacher': teacher,
    #             # 'questions': Exam.objects.all(),
    #             'course': form.cleaned_data.get('course'),
    #             # 'questions': Exam.objects.filter(course=subject1),
    #         }
    #         print("student", student)
    #         return render(request,'lecturers/question_list.html', context)
    # else: 
    #     context = {
    #         'form' : StudentListForm(),
    #         # 'teacher': teacher,
    #     }
    return render(request, 'lecturers/student_list.html', context)


    
    # context = {

    #     # 'questions': Exam.objects.all(),
    #     'semester': form.cleaned_data.get('semester'),
    #     'course': form.cleaned_data.get('course'),
    #     'level': form.cleaned_data.get('level'),
    #     # 'student': request.session['reg_no'],
    #     #                     
    #     'paper': paper,               
    #     'student': student,               
    #     'questions': Exam.objects.filter(course=subject1),

    # }





def login(request):
    return render(request, 'lecturers/login.html')



def teacherLogin(request):
    if request.method == 'POST':
        # teaId = request.POST.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print("id", teaId, "username", username, "password", password)
        print("username", username, "password", password)

        teacher = Teacher.objects.get(username=username)
        request.session['username'] = username
        # teachers = Teacher.objects.filter(id=teacher.id)
        print(teacher)
        # if (password == teacher.password1) and (username == teacher.username): 
            # paper = Paper.objects.filter(tid=teacher.id)
        sweetify.success(request, f'You successfully logged in')
        # return render(request,'lecturers/dashboard.html', {'teacher':teacher})
        return redirect(reverse('lecturer_dashboard'), {'teacher':teacher})
    else: 
        return render (request, 'exam/about.html', {'message': 'Incorrect password'})


# def profile(request):
#     username = request.session['username']
#     print("username::::::", username)
#     title = 'UserProfile'
#     teacher = Teacher.objects.get(username=username)
#     print("teacher::::::", teacher)
#     context = {
#         'teacher': teacher,
#         'title' : title
#     }
#     return render(request, 'lecturers/profile.html', context)


def profile(request):
    username = request.session['username']
    teacher = Teacher.objects.get(username=username)
    if request.method == 'POST':
        username = request.session['username']
        teacher = Teacher.objects.get(username=username)    
        u_form = TeacherUpdateForm(request.POST, instance=teacher)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=teacher.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('lecturer-profile')
    else:
        # return redirect('lecturer-profile')
        u_form = TeacherUpdateForm(instance=teacher)
        p_form = ProfileUpdateForm(instance=teacher.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'teacher': teacher

    }

    return render(request, 'lecturers/profile.html', context)


# def exam_delete_view(request, id):
#     username = request.session['username']
#     print("username::::::", username)

#     teacher = Teacher.objects.get(username=username)
#     print("teacher::::::", teacher)
#     context = {
#         'teacher': teacher
#     }

#     obj = get_object_or_404(Paper, id = id)

#     if request.method == "POST":
#         obj.delete()
#         return redirect(reverse('lecturer_dashboard'), {'teacher':teacher})
#     return render(request, "question_confirm_delete.html", context)

class ExamCreateView(SweetifySuccessMixin, CreateView):
    model = Exam
    form_class = ExamCreateForm
    template_name = 'lecturers/exam_form.html'
    context_object_name = Teacher
    success_message = 'Question successfully added!'

    def get_context_data(self, *args, **kwargs):
        username = self.request.session['username']
        context = super().get_context_data(*args,**kwargs)
        context['teacher'] = Teacher.objects.get(username=username)
        return context

    def form_valid(self, form):
        form.instance.lecturer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('exam-create')

    
 

class ExamSetupView(SweetifySuccessMixin, CreateView):
    model = Paper
    form_class = ExamSetupForm
    template_name = 'lecturers/exam_setup.html'
    context_object_name = Teacher
    success_message = 'Paper successfully created, Add Questions!'

    def get_context_data(self, *args, **kwargs):
        username = self.request.session['username']
        context = super().get_context_data(*args,**kwargs)
        context['teacher'] = Teacher.objects.get(username=username)
        return context

    def form_valid(self, form):
        form.instance.lecturer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('exam-create')

   


# class ExamDeleteView(DeleteView):
#     model =  Paper
#     # context_object_name = Teacher
#     # template_name = 'lecturers/examsetup_update.html'

#     def get_success_url(self):
#         return reverse('exam-create')

#     def test_func(self):
#         paper = self.get_object()
#         if self.request.teacher == paper.id:
#             return True
#         return False

#     # def get_context_data(self, *args, **kwargs):
#     #     username = self.request.session['username']
#     #     context = super().get_context_data(*args,**kwargs)
#     #     context['teacher'] = Teacher.objects.get(username=username)
#     #     return context

#     def get_absolute_url(self): # new
#         return reverse('exam-create', args=[str(self.id)])


# def studentLogin(request):
#     if request.method=='POST':
# # Get form information
#         stuId=request.POST.get('id')
#         password=request.POST.get('password')
#         print("id",stuId,"password",password)
# # Get the student entity by student number
#         student=models.Student.objects.get(id=stuId)
#         print(student)
#         if password == student.password: #Login successful
#     #Query test information
#             paper=models.Paper.objects.filter(major=student.major)
# #Query score information
#             grade=models.Grade.objects.filter(sid=student.id)
#     # render index template
#         return render(request,'index.html',{'student':student,'paper':paper,'grade':grade})

#     else: return render (request, 'index.html', {'message': 'Incorrect password'})