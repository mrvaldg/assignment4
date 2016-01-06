from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from as3.forms import *
from as3.models import *


def addteacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            a = Teacher(firstname=form.cleaned_data["firstname"],
                        lastname=form.cleaned_data["lastname"],
                        office_details=form.cleaned_data["office_details"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = TeacherForm()
    return render_to_response('addteacher.html', {'form': form},
                              RequestContext(request))


def addcourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            a = Course(name=form.cleaned_data["name"],
                       code=form.cleaned_data["code"],
                       classroom=form.cleaned_data["classroom"],
                       time=form.cleaned_data["time"],
                       teacher=form.cleaned_data["teacher"])
            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = CourseForm()
    return render_to_response('addcourse.html', {'form': form},
                              RequestContext(request))


def addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form2 = StudentToCourseForm(request.POST)
        if form.is_valid() and form2.is_valid():
            a = Student(firstname=form.cleaned_data["firstname"],
                        lastname=form.cleaned_data["lastname"],
                        email=form.cleaned_data["email"])
            a.save()
            c = Course.objects.get(id=form2.cleaned_data["courses"])
            a.courses.add(c)
            return HttpResponseRedirect('/all-students/')
    else:
        form = StudentForm()
        form2 = StudentToCourseForm()
    return render_to_response('addstudent.html', {'form': form, 'form2': form2},
                              RequestContext(request))


def allcourses(request):
    c = Course.objects.all()
    return render_to_response('allcourses.html', {'c':c}, RequestContext(request))


def allteachers(request):
    t = Teacher.objects.all()
    return render_to_response('allteachers.html', {'t':t}, RequestContext(request))



def allstudents(request):
    s = Student.objects.all()
    return render_to_response('allstudents.html', {'s':s}, RequestContext(request))

