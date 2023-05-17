from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.DateField()

class Subject(models.Model):
    title = models.CharField(max_length=100)
    clas = models.SmallIntegerField()

class Img(models.Model):
    name = models.CharField(max_length=100)
    img = models.FileField(upload_to="ava", null=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    clas = models.SmallIntegerField()
    img = models.ForeignKey(Img, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=14)
    social_network = models.CharField(max_length=1000)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    date_of_bearth = models.DateField(null=True)

    def __str__(self):
        return self.fullname

class Journal(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.SmallIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

class InfoStudent(models.Model):
    info = models.TextField()
    img = models.ForeignKey(Img, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.info


class Teacher(models.Model):
    fullname = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ForeignKey(Img, on_delete=models.CASCADE)

class Clas(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    number = models.SmallIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="classes")

class StudyTime(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_lesson = models.TimeField()
    end_lesson = models.TimeField()
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)




