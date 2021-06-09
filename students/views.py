from django.shortcuts import render, redirect, reverse, get_object_or_404, resolve_url
from django.contrib import messages
from exam.models import Student, Paper, Teacher, Exam, Grade
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import sweetify
from exam.models import models
from django.db import models
from .forms import StudentRegisterForm
from .forms import ExamForm, LoginForm
from django.contrib import messages
from django.contrib.auth.views import LoginView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'students/demo.html')


# @login_required
# def dashboard(request):
#     return render(request, 'students/demo.html')


def result(request):
    return render(request, 'students/result.html')




# def info(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         # username: ''
#         if form.is_valid():
#             form.save()
#             name: form.cleaned_data.get('name')
#             messages.success(request, f'Your account has been created! You can now login')
#             # return render(request, 'students/login.html')
#             return redirect('students-login')
#     else:
#         form = ContactForm()
#     return render(request, template_name="students/start_exam.html", context={'form': form})

# def login(request):
#     return render(request, 'students/login.html')


# def startExam(request):
#     return render(request, 'students/start_exam.html', {'form': form})




# def studentLogin(request):
#     if request.method == "POST":
#         form = AuthenticationLoginForm(request, data=request.POST)
#         if form.is_valid():
#             print ("Hello world")
#             name = form.cleaned_data.get('id')
#             password = form.cleaned_data.get('password')
#             user = authenticate(name=name, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as")
#                 return redirect("main:homepage")
#             else:
#                 messages.error(request,"Invalid Matric No.")
#         else:
#             print ("Fuck off")
#             messages.error(request,f'Print Error')
#     form = AuthenticationLoginForm()
#     return render(request=request, template_name="students/login.html", context={"form":form})

# def studentLogin(request):
#     # context = RequestContext(request)
#     if request.method == 'POST':
#         stuId = request.POST.get('reg_no')
#         password = request.POST.get('password')
#         print("reg_no",stuId,"password",password)
#         user = authenticate(stuId=stuId, password=password)
#         student = Student.objects.get(id=stuId)
#         if (user is not None) and (password == student.password):
#             if user.is_active:
#                 login(request, user)
#                 messages.info(request, f'You are now logged in as')
#                 return HttpResponseRedirect("exam/home")
#             else:
#                 messages.error(request,"Invalid Matric No.")
#         else:
#             print ("invalid login details" + stuId + " " + password)
#             messages.success(request, f'You are logged in ')
#             return render(request, 'students/start_exam.html', {'student':student})
#     else:
#         return render(request, 'students/login.html', {'message': 'Incorrect password'})


    
        
# if (password == student.password):
#             messages.success(request, f'You are ')
#             return render(request, 'students/start_exam.html', {'student':student})

#         else:
#             print ("invalid login details" + stuId + " " + password)
#             messages.success(request, f'You are ')
#             return render(request, 'students/login.html', {'student':student})

# def studentLogin(request):
#     if request.method == 'POST':
#         stuId = request.POST.get('reg_no')
#         password = request.POST.get('password')
#         student = authenticate(request, stuId=stuId, password=password)
#         print(student)
#         if student is not None:
#             studentlogin(request, student)
#             messages.success(request, f'{stuId}, You are logged in! ')  
#             return render(request,'students/start_exam.html')
#         else:
#             return render (request, 'exam/about.html', {'message': 'Incorrect password'})

# class MyLoginView(LoginView):
#     authentication_form = LoginForm
#     template_name = 'students/login.html'
#     redirect_authenticated_user = True

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         msg = {'uhuhujhkhkhkhku'}
#         context['msg'] = msg.get(self.request.GET.get('kjjijkjkj'), '')
#         return context

#     def get_success_url(self):
#  
#        return resolve_url('startexam')



def register(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        # username: ''
        if form.is_valid():
            form.save()
            name: form.cleaned_data.get('name')
            messages.success(request, f'Your account has been created!')
            # return render(request, 'students/login.html')
            return redirect('students-login')
    else:
        form = StudentRegisterForm()
    return render(request, 'students/register.html', {'form': form})


def studentLogin(request):
    if request.method=='POST':
        stuId = request.POST.get('reg_no')
        password = request.POST.get('password')
        print("reg_no",stuId,"password",password)
        student = Student.objects.get(id=stuId)
        print(student)
        form = ExamForm(request.POST)
        
        if password == student.password1: #Login successful

            request.session['reg_no'] = stuId


            global Val
            def val():
                return stuId
    # #Query test information
            # paper = Paper.objects.get(Tid=student.id)
            paper = Paper.objects.filter(major=student.major)
    # #Query score information
            grade = Grade.objects.filter(sid=student.id)
    # # render index template
            
            # return HttpResponseRedirect(reverse('startexam', kwargs={'student':student})) 
            sweetify.success(request, f'Welcome, {stuId}! You are logged in! ')
            
            return render(request,'students/start_exam.html', {'student':student, 'grade':grade, 'paper':paper, 'form':form})
            # return redirect(reverse('startexam', kwargs={'student':student}))
            # return redirect('startexam')

    else: 
        return render (request, 'exam/about.html', {'message': 'Incorrect password'})

        
def examstart(request):
    if request.session.has_key('reg_no'):
        if request.method=='POST':
            form = ExamForm(request.POST)
        # username: ''
            if form.is_valid():
                # form.save()
                # semester: form.cleaned_data.get('semester')
                # course: form.cleaned_data.get('course')
                # level: form.cleaned_data.get('level')

                # semester = request.POST.get('semester')
                # course = request.POST.get('course')
                # level = request.POST.get('level')
                # student = level
                # print("semester", semester)
                # print("course", course)
                # print("level", level)
                stuId = request.session['reg_no']
                student = Student.objects.get(id=stuId)
                subject1 = request.POST.get('course')
                level = request.POST.get('level')
                semester = request.POST.get('semester')
                print('level', level)
                paper = Paper.objects.get(course=subject1, level=level, semester=semester)
                print("student::::::", student, paper.instruction)
                
                # if paper 
                
                context = {

                    # 'questions': Exam.objects.all(),
                    'semester': form.cleaned_data.get('semester'),
                    'course': form.cleaned_data.get('course'),
                    'level': form.cleaned_data.get('level'),
                    # 'student': request.session['reg_no'],
                    #                     
                    'paper': paper,               
                    'student': student,               
                    'questions': Exam.objects.filter(course=subject1),

                }

                # messages.success(request, f'Your account has been created!')
            # return render(request, 'students/login.html')
                print("subject1", subject1)
            # stuId=val()
                student = request.session['reg_no']
                # context = {
                #     'student': request.session['reg_no']
                # }{'message': 'Incorrect password', 'student': student}
                print("student",student)
                # messages.success(request, f'You can now take your ')
                # return redirect('exam-home')
                return render(request,'exam/home.html', context)

        else: 
            return render (request, 'exam/about.html', {'message': 'Incorrect password', 'student': student})
    else:
        return render (request, 'students/about.html', {'message': 'Incorrect password'})



#Teachers query students according to conditions
def queryStudent(request):
    #Get the condition value of teacher query
    sid=request.GET.get('id')
    sex=request.GET.get('sex')
    course=request.GET.get('course')

    #Get the id of the teacher
    tid=request.GET.get('tid')
    teacher = Teacher.objects.get(id=tid)
    
    paper = Paper.objects.filter(tid=teacher.id)

    # print(sid,sex,subject)
    from django.db import connection,transaction
    cursor=connection.cursor()
    sql="select * from grade,student where student.id=grade.sid_id " \
        "and student.id like %s and grade.subject like %s and student.sex like %s and '1'='1'"
    val=('%'+sid+'%','%'+course+'%','%'+sex+'%')
    cursor.execute(sql,val)
    result=dictfetchall(cursor)

    # print(result)
    return render(request,'teacher.html',{'teacher':teacher,'result':result,'paper':paper})

#Convert the results found using native SQL statements from tuple type to dictionary type
def dictfetchall(cursor):
    "Save the result returned by the cursor to a dictionary object"
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]


def calGrade(request):
    
    if request.method=='POST':
        # Get student number and subject
        sid=request.POST.get('sid')
        subject1 = request.POST.get('subject')

        print("sid", sid )
        print("subject1", subject1 )
        # Regenerate Student instance, Paper instance, Grade instance, the name is consistent with the for in index, and can be rendered repeatedly
        student= Student.objects.get(id=sid)
        paper = Paper.objects.filter(major=student.major)
        grade = Grade.objects.filter(sid=student.id)
        print("student = ", student)
        print("paper = ", paper)
        print("grade = ", grade)
        # Calculate student scores for the exam
        question = Paper.objects.filter(course=subject1).values("pid").values('pid__id', 'pid__answer','pid__score')
        print("question = ", question)
        print("subject1", subject1 )
        mygrade=0 #Initialize a score of 0
       
        for p in question:
            qId=str(p['pid__id']) #int to string, find the question number through pid
            print('qId', qId)
            myanswer=request.POST.get(qId) #Get students' answers on this question through qid
            # print(myans)
            print("myanswer::::", myanswer)
            answer=p['pid__answer'] # Get the correct answer

            # print(okans)
            print("answer::::", answer)
            if myanswer==answer: #Judge whether the student's answer is consistent with the correct answer

                # mygrade+=5#If they are consistent, get the score of the question and accumulate the mygrade variable
                mygrade+=p['pid__score']#If they are consistent, get the score of the question and accumulate the mygrade variable

        
        if mygrade < 40 :
            score = 'F'
            print(score)
        elif mygrade < 45:
            score = 'E'
            print(score)
        elif mygrade < 50 :
            score = 'D'
            print(score)
        elif mygrade <= 60 :
            score = 'C'
            print(score)
        elif mygrade <= 70 :
            score = 'B'
            print(score)
        elif mygrade <= 100 :
            score = 'A'
            print(score)

        #Insert data into the Grade table
        Grade.objects.create(sid_id=sid,subject=subject1,grade=mygrade,score=score)
        print("my sid = ", sid)
        print("my subject = ", subject1)
        print("my grade = ", mygrade)

        context = {
            'student':student,
            'paper':paper,
            'grade':grade,
            'score':score,
            'mygrade': mygrade,
            'subject' : subject1
        }
        return render(request,'students/result.html', context)

# def startExam(request):
#     student = get_object_or_404(Student)
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         # username: ''
#         # if form.is_valid():
#         #     form.save()
#         #     name: form.cleaned_data.get('name')
#         #     messages.success(request, f'Your account has been created! You can now login')
#         #     # return render(request, 'students/login.html')
#         #     return redirect('students-login')
#     else:
#         form = ContactForm()
#     return render(request, template_name="students/start_exam.html", context={'form': form, 'student':student})