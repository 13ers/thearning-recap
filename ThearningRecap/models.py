from django.db import models

class UserInfo(models.Model):
    user_id = models.CharField(unique=True, max_length=255)
    user = models.ForeignKey(User)
    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fullname} {user_id}"

class Class(models.Model):
    major = models.CharField(max_length=255)
    level = models.IntegerField()
    serial = models.IntegerField()

    def __str__(self):
        if self.level == 10:
            return f"X-{major} {serial}"
        elif self.level == 11:
            return f"XI-{major} {serial}"
        elif self.level == 12:
            return f"XII-{major} {serial}"

class Teacher(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    user = models.ForeignKey(UserInfo, on_delete=models.PROTECT)

class Homeroom(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    user = models.ForeignKey(UserInfo, on_delete=models.PROTECT)

class Student(models.Model):
    classroom = models.ForeignKey(Class, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    