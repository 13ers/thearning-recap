from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    uid = models.CharField(unique=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fullname} {self.user_id}"

class Course(models.Model):
    course_id = models.IntegerField(unique=True, auto_created=True)
    name = models.CharField(max_length=255)

class Class(models.Model):
    major = models.CharField(max_length=255)
    level = models.IntegerField()
    serial = models.IntegerField()

    def __str__(self):
        if self.level == 10:
            return f"X-{self.major} {self.serial}"
        elif self.level == 11:
            return f"XI-{self.major} {self.serial}"
        elif self.level == 12:
            return f"XII-{self.major} {self.serial}"

class Teacher(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    user = models.ForeignKey(UserInfo, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

class Homeroom(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    user = models.ForeignKey(Teacher, on_delete=models.PROTECT)

class Student(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    