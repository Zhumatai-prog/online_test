from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from quiz import models as QMODEL
from teacher import models as TMODEL
from .models import *
from quiz.models import *


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin')
    return render(request,'student/studentsignup.html',context=mydict)

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_dashboard_view(request):
    dict={

    'total_course':QMODEL.Course.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    }
    return render(request,'student/student_dashboard.html',context=dict)

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_exam_view(request, pk):
    student = Student.objects.get(user_id=pk)
    courses = Course.objects.all()
    clist = []
    for course in courses:
        if student.dept in course.dept.all() and student.position in course.position.all():
                clist.append(course)

    return render(request,'student/student_exam.html', {'courses': courses,
                                                        'student': student,
                                                        'clist': clist})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def take_exam_view(request,pk):
    course=QMODEL.Course.objects.get(id=pk)
    total_questions=QMODEL.Question.objects.all().filter(course=course).count()
    questions=QMODEL.Question.objects.all().filter(course=course)
    total_marks = 0
    for i in questions:
        for a in i.answer:
            total_marks = total_marks + 1

    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def start_exam_view(request,pk):
    course = Course.objects.get(id=pk)
    questions = Question.objects.all().filter(course=course)
    if request.method=='POST':
        pass

    response = render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def calculate_marks_view(request):
    if request.COOKIES.get('course_id') is not None:
        if request.method == 'POST':

            course_id = request.COOKIES.get('course_id')
            course = QMODEL.Course.objects.get(id=course_id)
            total_marks = 0
            questions = Question.objects.all().filter(course=course)
            response = HttpResponseRedirect('view-result')
            for i in range(len(questions)):

                    selected_ans = request.POST.get(str(i+1))
                    actual_answer = questions[i].answer

                    #print(request.POST.get('1'))
                    #print(actual_answer)

                    if selected_ans is None:
                        pass
                    elif selected_ans in actual_answer:
                        total_marks = total_marks + 1
                        response.delete_cookie(str(i+1))
                    elif selected_ans == questions[i].entry_answer:
                        total_marks = total_marks + 1
                        response.delete_cookie(str(i+1))
                    response.delete_cookie(str(i+1))
        response.delete_cookie('course_id')
        student = Student.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks=total_marks
        result.exam=course
        result.student=student
        result.save()

        return HttpResponseRedirect('view-result')



@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def view_result_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})


@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def check_marks_view(request,pk):
    course = Course.objects.get(id=pk)
    student = Student.objects.get(user_id=request.user.id)
    results = Result.objects.all().filter(exam=course).filter(student=student)
    questions = Question.objects.all().filter(course=course)
    total_marks = 0
    for a in questions:
        for b in a.answer:
            total_marks = total_marks + 1
    return render(request,'student/check_marks.html',{'results':results, 'total_marks': total_marks})

@login_required(login_url='studentlogin')
@user_passes_test(is_student)
def student_marks_view(request):
    courses=QMODEL.Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})
