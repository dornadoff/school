from django.db import models
from django.contrib.auth.models import User

class Img(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField(upload_to="ava")

class Student(models.Model):
    i_f_o = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    clas = models.SmallIntegerField()
    img = models.ForeignKey(Img, on_delete=models.CASCADE)
    number = models.CharField(max_length=14)
    social_network = models.CharField(max_length=1000)

class InfoStudent(models.Model):
    info = models.TextField()
    img = models.ForeignKey(Img, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
