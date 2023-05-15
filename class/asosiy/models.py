from django.db import models
from django.contrib.auth.models import User

class Img(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField(upload_to="ava", null=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    i_f_o = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    clas = models.SmallIntegerField()
    img = models.ForeignKey(Img, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=14)
    social_network = models.CharField(max_length=1000)
    def __str__(self):
        return self.i_f_o

class InfoStudent(models.Model):
    info = models.TextField()
    img = models.ForeignKey(Img, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.info
