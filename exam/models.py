from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


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



LEVEL = (
        ("-----", "-----"),
        ("100", "100"),
        ("200", "200"),
        ("300", "300"),
        ("400", "400"),
    )

class Student(models.Model):
    id = models.CharField('Reg No.', max_length=20, primary_key=True)
    name = models.CharField('Name', max_length=50)
    sex = models.CharField('Gender', max_length=10, choices=SEX, default='Male')
    dept = models.CharField('Department', max_length=100, choices=DEPT, default=None)
    major = models.CharField('Major', max_length=100, default=None)
    level = models.CharField('Level', max_length=10, default=None, null=True)
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
    # image = models.ImageField('image')
    # question = models.TextField()
    course = models.CharField('Course', max_length=20, default='', help_text='Must be all CAPS')
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    # date_posted = models.DateTimeField(default=timezone.now)
    # lecturer = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField('score', default=1)

    objects = models.Manager()
    
    def __str__(self):
        # return self.question
        return '<%s:%s>' % (self.course, self.question)

    class Meta:
        db_table = 'question'

        verbose_name = 'Question Bank'
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
    dept = models.CharField('Department', max_length=100, choices=DEPT, default=None)
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
    course = models.CharField(
        ('Course'), max_length=20, unique=True, error_messages={'unique': ("The Course has already been created, Add Questions!"),
        }, default=''
    )
    course_title = models.CharField('Course Title', max_length=100, default='')
    instruction = RichTextField(default='')
    level = models.CharField('Level', max_length=10, choices=LEVEL, default='')
    semester = models.CharField('Semester', max_length=15, choices=SEMESTER, default='')
    major = models.CharField('Applicable for test papers', max_length=20)
    unit = models.IntegerField('Units', default=1)
    exam_time = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.major

    class Meta:
        db_table = 'paper'

        verbose_name = 'Exam paper'
        verbose_name_plural = verbose_name


class Grade(models.Model):
    sid = models.ForeignKey(Student, on_delete=models.CASCADE, default='')
    subject = models.CharField('Subject', max_length=20, default='')
    grade = models.IntegerField()
    score = models.CharField('Score', max_length=20, default='')

    objects = models.Manager()
    
    def __str__(self):
        return self.sid.name
                # return '<%s:%s>' % (self.student.name, self.sid, self.grade)

    class Meta:
        db_table = 'grade'

        verbose_name = 'Grade'
        verbose_name_plural = verbose_name


class Course(models.Model):
    tid = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.CharField(
        ('Course'), max_length=20, unique=True, error_messages={'unique': ("The Course has already been created, Add Questions!"),
        }, default=''
    )

    objects = models.Manager()

    def __str__(self):
        return self.course

    class Meta:
        db_table = 'course'

        verbose_name = 'Teacher course'
        verbose_name_plural = verbose_name


# class Course(models.Model):
#     id = models.AutoField(primary_key=True)
#     course_code = models.CharField('Course Code', max_length=20)
#     course_title = models.CharField('Course Title', max_length=100)

#     objects = models.Manager()

#     def __str__(self):
#         return self.course_code
#                 # return '<%s:%s>' % (self.student.name, self.sid, self.grade)

#     class Meta:
#         db_table = 'Course Code'

#         verbose_name = 'Course Code'
#         verbose_name_plural = verbose_name



