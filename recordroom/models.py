from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
# Create your models here.

class recording(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    audio = models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT))
    title = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.title