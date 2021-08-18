from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from exam.models import Student
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.forms import StudentCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _


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

SEMESTER = (
        ("1st Semester", "1st Semester"),
        ("2nd Semester", "2nd Semester"),
    )

COURSE = (
        (" ", " "),
        ("COS101", "COS101"),
        ("COS203", "COS203"),
        ("COS211", "COS211"),
        ("COS441", "COS441"),
        ("COS431", "COS431"),
        ("COS461", "COS461"),
        ("COS102", "COS102"),

    )


LEVEL = (
        ("100", "100"),
        ("200", "200"),
        ("300", "300"),
        ("400", "400"),
    )


class StudentRegisterForm(StudentCreationForm):
    id = forms.CharField(label='Matriculation Number', max_length=20, widget=forms.TextInput(
            attrs={
                # "placeholder" : "Matriculation Number",                
                # "class": "form-control",
                "autocomplete": "off"
            }
        ))
    name = forms.CharField(label='Name', max_length=100,
    widget=forms.TextInput(
            attrs={
                # "placeholder" : "Enter Your Name",                
                # "class": "form-control",
                "autocomplete": "off"
            }
        ))
    sex = forms.ChoiceField(choices=SEX)
    dept = forms.ChoiceField(label='Department', choices=DEPT)
    major = forms.ChoiceField(label='Major', choices=DEPT)
    level = forms.CharField(label='Level', max_length=10)
    email = forms.EmailField()
    # birth = forms.DateField()


    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'sex',
            'dept',
            'major',
            'level',
            'email',
            'password1',
            'password2'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image'
        ]


class ExamForm(forms.Form):
        semester = forms.ChoiceField(choices=SEMESTER, required=False, label='Semester', help_text="Select your semester")
        course = forms.ChoiceField(choices=COURSE, required=False, label='Course', initial=None, help_text="Choose the course you wish to offer")
        level = forms.ChoiceField(choices=LEVEL, required=False, label='Choose your level')       
        class Meta:
            fields = [
                'semester',
                'course',
                'level',
            ]


class LoginForm(AuthenticationForm):
    # yourname = forms.CharField(max_length=100, required=False, label='Your Name')
    # email = forms.EmailField(required=False, label='Your Email Address')
    stuid = forms.ChoiceField(widget=TextInput(attrs={'placeholder':'matric no'}))
    password = forms.ChoiceField(widget=PasswordInput(attrs={'placeholder':'matric no'}))

    class Meta:
        # model = Student
        fields = [
            'stuid',
            'password',
        ]