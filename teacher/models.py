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


