from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from django.urls import reverse

from users.models import ThearningUser
from users.models import Student

def dashboard_view(request):

    try:
        user_info = ThearningUser.objects.filter(uid=request.user.uid).first()
    except User.DoesNotExist:
        user_info = None

    first_name = user_info.first_name

    if user_info is None:
        return redirect("login")

    if user_info.status == "admin":
        return render(request, "admin/admin.html", {"user_info":user_info, "first_name":first_name})

    elif user_info.status == "homeroom":
        return render(request, "hrteacher/hrTeacher.html", {"user_info":user_info, "first_name":first_name})

    elif user_info.status == "teacher":
        return render(request, "teacher/user.html", {"user_info": user_info, "first_name":first_name})

@staff_member_required
def teacher_data_view(request):
    return render(request, "teacher.html")

@staff_member_required
def add_teacher_view(request):
    get = request.POST.get
    if request.method == "POST":
        username = get('username')
        password = get('password')
        uid = get('uid')
        gender = get('gender')
        level = get('level')
        course = get('course')

        User.objects.create_user(

        )
        ThearningUser.objects.create(

        )

    return render(request, "addTeacher.html")
    

def students_list(request):

    students = Student.objects.all()

    return render(request, "student.html",{"students":students})



