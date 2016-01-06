from __future__ import unicode_literals
from django.db import models


class Teacher(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    office_details=models.CharField(max_length=120)
    phone=models.PositiveIntegerField()
    email=models.EmailField(max_length=120)
    def __unicode__(self):
        return "{0} {1}".format(self.firstname,self.lastname)


class Course(models.Model):
    name=models.CharField(max_length=120)
    code=models.CharField(max_length=120)
    classroom=models.CharField(max_length=120)
    time=models.TimeField(max_length=120)
    teacher=models.OneToOneField(Teacher)
    def __unicode__(self):
        return self.name


class Student(models.Model):
    firstname=models.CharField(max_length=120)
    lastname=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    courses=models.ManyToManyField(Course)
    def __unicode__(self):
        return "{0} {1}".format(self.firstname,self.lastname)