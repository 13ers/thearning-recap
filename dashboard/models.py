from django.db import models

from users.models import *

class Report(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    knowledge_mark = models.IntegerField()
    skills_mark = models.IntegerField()
    total_mark = models.IntegerField()