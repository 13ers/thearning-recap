from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from .managers import ThearningUserManager


class ThearningUser(AbstractUser):
    username = None
    uid = models.CharField(unique=True, max_length=20)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    gender = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

    USERNAME_FIELD = 'uid'
    objects = ThearningUserManager()

    @property
    def is_student(self):
        return self.status == "student"

    @property
    def is_teacher(self):
        return self.status == "teacher"

    @property
    def is_admin(self):
        return self.status == "admin"


    def __str__(self):
        return self.uid


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
    user = models.ForeignKey(ThearningUser, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)


class Homeroom(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    user = models.ForeignKey(Teacher, on_delete=models.PROTECT)


class Student(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
