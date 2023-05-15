from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class HomePage(View):
    def get(self, request):
        return render(request, "home.html")

class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
            user = authenticate(request, username=request.POST.get("username"),
                                password=request.POST.get("password"))
            if user is None:
                return redirect("/login/")
            login(request, user)
            return redirect("/student/2/")

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        b = User.objects.filter(
            username=request.POST.get("username")
        )
        if len(b) < 1:

            Student.objects.create(
                i_f_o=request.POST.get("fullname"),
                user=User.objects.create_user(
                    username=request.POST.get("username"),
                    password=request.POST.get("password")
                ),
                clas=9,
                img=Img.objects.create(
                    name=f"{request.POST.get('fullname')}",
                    img=request.FILES.get("image")),
            )
            return redirect(f"/student/{Student.objects.last().id}/")
        return HttpResponse(" <center> <h1>Извените но этот аккаунт уже существует</h1> </center>")


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
            info = {"info": "Нет изображений"}
        data = {
            "student": student,
            "info": info,
        }
        print(data)
        return render(request, "student.html", data)

class InfoStudentAdd(View):
    def get(self, request, gt):
        data = {
            "student": Student.objects.get(id=gt)
        }
        return render(request, "add-student-info.html", data)

    def post(self, request, gt):
        if request.FILES.get("image") is None:
            return redirect("/error/form/")
        InfoStudent.objects.create(
            info = request.POST.get("info"),
            img = Img.objects.create(
                name="a",
                img=request.FILES.get("image")
            ),
            student=Student.objects.get(id=gt)
        )
        return redirect(f"/student/{gt}/")

class ErrorFormView(View):
    def get(self, request):
        return render(request, "error-form.html")
