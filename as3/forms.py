
from django import forms

from as3.models import Teacher, Course


class TeacherForm(forms.Form):
    firstname=forms.CharField(max_length=120)
    lastname=forms.CharField(max_length=120)
    office_details=forms.CharField(max_length=120)
    phone=forms.IntegerField()
    email=forms.EmailField(max_length=120)


class CourseForm(forms.Form):
    name=forms.CharField(max_length=120)
    code=forms.CharField(max_length=120)
    classroom=forms.CharField(max_length=120)
    time=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    teacher=forms.ModelChoiceField(Teacher.objects.all())


class StudentForm(forms.Form):
    firstname=forms.CharField(max_length=120)
    lastname=forms.CharField(max_length=120)
    email=forms.EmailField(max_length=120)

class StudentToCourseForm(forms.Form):
    courses=forms.ModelMultipleChoiceField(Course.objects.all())