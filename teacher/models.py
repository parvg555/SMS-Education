from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.


class classroom(models.Model):
    teacher = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100,null = False, blank = False)
    subject = models.CharField(max_length = 100,null=False, blank=False)

    def __str__(self):
        return self.name


class student(models.Model):
    classroom = models.ForeignKey(classroom,null=False,blank=False,on_delete = models.CASCADE)
    name = models.CharField(max_length=100,null=False,blank=False)
    phone = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

class question(models.Model):
    classroom = models.ForeignKey(classroom,null=False,blank=False,on_delete=models.CASCADE)
    question = models.CharField(max_length = 200, null=False, blank = False)
    option1 = models.CharField(max_length = 50, null=False, blank = False)
    option2 = models.CharField(max_length = 50, null=False, blank = False)
    option3 = models.CharField(max_length = 50, null=False, blank = False)
    option4 = models.CharField(max_length = 50, null = False, blank = False)
    correct = models.CharField(max_length = 10, null = False, blank = False)

    def __str__(self):
        return self.question

class doubt(models.Model):
    classroom = models.ForeignKey(classroom, null = False, blank = False, on_delete = models.CASCADE)
    student = models.ForeignKey(student, null=False, blank = False, on_delete = models.CASCADE)
    question = models.CharField(max_length = 200, null=False, blank = False)
    answered = models.BooleanField (default = False)
    answer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.question


class answer(models.Model):
    question = models.ForeignKey(question, null = False, blank = False,  on_delete = models.CASCADE)
    student = models.ForeignKey(student, null=False, blank = False, on_delete = models.CASCADE)
    answer = models.CharField(max_length = 10, null=False, blank = False)
    correct = models.BooleanField(default = False)
    
    def __str__(self):
        return self.answer
    


