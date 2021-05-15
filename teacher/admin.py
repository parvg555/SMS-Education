from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(classroom)
admin.site.register(student)
admin.site.register(question)
admin.site.register(doubt)
admin.site.register(answer)