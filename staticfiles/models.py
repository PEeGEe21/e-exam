from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



DEPT = (
        ("Maths_&_Comp", "Maths and Computer Science"),
        ("BioChem", "BioChemistry"),
        ("Accounting", "Accounting"),
        ("Economics", "Economics"),
        ("History", "History"),
        ("Mass Commuication", "Mass Commuication"),
    )

SEX = (
        ("Male", "Male"),
        ("Female", "Female"),
    )


class Student(models.Model):
    id = models.CharField('Reg No.', max_length=20, primary_key=True)
    name = models.CharField('Name', max_length=20)
    sex = models.CharField('Gender', max_length=10, choices=SEX, default='Male')
    dept = models.CharField('Department', max_length=100, choices=DEPT, default='')
    major = models.CharField('Major', max_length=20, default=None)
    email = models.EmailField('Email', default=None)
    password1 = models.CharField('Password', max_length=10, default='111111')
    password2 = models.CharField('Password2', max_length=10, default='111111')
    # birth = models.DateField('Date Of Birth')


    objects = models.Manager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'name'
    set_password = 'password'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk":self.pk})

    class Meta:
        db_table = 'student'
        verbose_name = 'student'

        verbose_name_plural = verbose_name


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    question = RichTextField(default='')
    # question = models.TextField()
    course = models.CharField('Course', max_length=20, default='')
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    # date_posted = models.DateTimeField(default=timezone.now)
    # lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField('score', default=1)

    def __str__(self):
        # return self.question
        return '<%s:%s>' % (self.course, self.question)

    class Meta:
        db_table = 'question'

        verbose_name = 'Examination Question Bank'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    # id = models.CharField("Teacher ID", max_length=20, primary_key=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=20)
    # username = models.CharField('Username', max_length=20, default='')
    username = models.CharField(
        ('username'), max_length=150, unique=True, error_messages={'unique': ("A user with that username already exists."),
        },
    )
    sex = models.CharField('Gender', max_length=10, choices=SEX, default='Male')
    dept = models.CharField('Department', max_length=20, choices=DEPT, default=None)
    email = models.EmailField('Email', default=None)
    password1 = models.CharField('Password', max_length=20, default='000000')
    password2 = models.CharField('Password2', max_length=20, default='000000')


    objects = models.Manager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    set_password = 'password'
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Teacher'

        verbose_name_plural = verbose_name


class Paper(models.Model):
    pid = models.ManyToManyField(Exam)
    tid = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.CharField('Course', max_length=20, default='')
    instruction = models.TextField()
    major = models.CharField('Applicable for test papers', max_length=20)
    exam_time = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return self.major

    class Meta:
        db_table = 'paper'

        verbose_name = 'Test paper'
        verbose_name_plural = verbose_name


class Grade(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    subject = models.CharField('Subject', max_length=20, default='')
    grade = models.IntegerField()

    def __str__(self):
        return self.sid.name
                # return '<%s:%s>' % (self.student.name, self.sid, self.grade)

    class Meta:
        db_table = 'grade'

        verbose_name = 'Achievement'
        verbose_name_plural = verbose_name



