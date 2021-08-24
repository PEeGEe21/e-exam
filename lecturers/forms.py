from django import forms
from django.contrib.auth.models import User
from exam.models import Teacher
from exam.models import Exam
from exam.models import Paper
from exam.models import Course
from exam.models import Student
from django.http import HttpResponse
from django.db import models
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import TeacherCreationForm
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

COURSE = (
        (" ", " "),
        ("COS203", "COS203"),
        ("COS211", "COS211"),
        ("COS441", "COS441"),
        ("COS431", "COS431"),
        ("COS461", "COS461"),
        ("COS101", "COS101"),
        ("COS102", "COS102"),
    )

DEPT = (
        ("Mathematics", "Mathematics"),
        ("Computer Science", "Computer Science"),
        ("BioChemistry", "BioChemistry"),
        ("Accounting", "Accounting"),
        ("Economics", "Economics"),
        ("History", "History"),
        ("Microbiology", "Microbiology"),
        ("Mass Commuication", "Mass Commuication"),
        ("International Relations", "International Relations"),
        ("Criminology", "Criminology"),
        ("Language and Linguistics", "Language and Linguistics"),
    )

SEX = (
        ("Male", "Male"),
        ("Female", "Female"),
    )


class TeacherRegisterForm(forms.ModelForm):
    # id = forms.CharField(label='Teacher ID', max_length=20)
    name = forms.CharField(label='Name', max_length=100)
    username = forms.CharField(label='Username', max_length=50)
    sex = forms.ChoiceField(choices=SEX)
    dept = forms.ChoiceField(label='Department', choices=DEPT)
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = [
            # 'id',
            'name',
            'username',
            'sex',
            'dept',
            'email',
            'password1',
            'password2'
        ]

class TeacherUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = [
            'name',
            'sex',
            'dept',
            'email',
        ]



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image',
            'coverimage'
        ]


# class LoginForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder" : "Username",                
#                 "class": "form-control"
#             }
#         ))
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder" : "Password",                
#                 "class": "form-control"
#             }
#         ))

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder" : "Username",                
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder" : "Email",                
#                 "class": "form-control"
#             }
#         ))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder" : "Password",                
#                 "class": "form-control"
#             }
#         ))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder" : "Password check",                
#                 "class": "form-control"
#             }
#         ))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')




class ExamCreateForm(forms.ModelForm):
    question = forms.CharField(
        widget=CKEditorWidget(attrs={
                "placeholder" : "Enter your question",                
                "class": "form-control col-12 col-lg-6 col-sm-12"
            }))
   
    class Meta:
        model = Exam
        fields = '__all__'
        # fields = ('question', 'course', 'option1', 'option2', 'option3', 'option4', 'answer', 'score' )
        template_name = 'lecturers/exam_form.html'


class ExamListForm(forms.Form):
        course = forms.ChoiceField(choices=COURSE, required=False, label='Course', initial=None, help_text="Choose the course you wish to view")
        class Meta:
            fields = [
                'course',
            ]

class StudentReportForm(forms.Form):
        # course = forms.ModelChoiceField(queryset=Course.objects.all(),required=False, label='Course', initial=None, help_text="Choose the course you wish to view")
        course = forms.CharField(required=False, label='Course', initial=None, help_text="Choose the course you wish to view")
        class Meta:
            fields = [
                'course',
            ]


class StudentListForm(forms.Form):
        student = forms.CharField(required=False, label='Course', initial=None, help_text="Choose the course you wish to view")
        class Meta:
            fields = [
                'student',
            ]


class ExamSetupForm(forms.ModelForm):
    tid = forms.ModelChoiceField(label='Teacher', queryset=Teacher.objects.all(), initial=None)
    exam_time = forms.DateTimeField(help_text="<b>2021-10-25 09:00:00</b> is the required Date/Time Format", 
    widget=forms.TextInput(
            attrs={
                "placeholder" : "Enter the Date/Time",                
                "class": "form-control"
            }
        ))
    class Meta:
        model = Paper
        # fields = '__all__'
        fields = ('tid', 'course', 'course_title', 'instruction', 'level', 'semester', 'major', 'exam_time', 'unit')
        template_name = 'lecturers/exam_setup.html'

class CourseCreateForm(forms.ModelForm):
    tid = forms.ModelChoiceField(label='Teacher', queryset=Teacher.objects.all(), initial=None)
    course = forms.CharField(required=False)
    class Meta:
        model = Course
        fields = '__all__'
        template_name = 'lecturers/setting.html'


