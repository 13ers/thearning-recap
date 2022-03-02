from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(ThearningUser)
admin.site.register(Homeroom)
admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)