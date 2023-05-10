from django.shortcuts import render
from django.views import View

from .models import *

class HomePage(View):
    def get(self, request):
        return render(request, "home.html")

class StudentsView(View):
    def get(self, request, gt):
        data = {
            "student": Student.objects.filter(clas=gt)
        }
        return render(request, "students.html", data)

class StudentView(View):
    def get(self, request, gt):
        student = Student.objects.get(id=gt)
        info = InfoStudent.objects.filter(student=student)
        if len(info) < 1:
            info = {"info": {"info":"Net infi"}}
        data = {
            "student": student,
            "info": info,
        }
        return render(request, "student.html", data)