from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from django.urls import reverse

from users.models import ThearningUser
from users.models import Student, Teacher

def dashboard_view(request):

    try:
        user_info = ThearningUser.objects.filter(uid=request.user.uid).first()
    except User.DoesNotExist:
        user_info = None

    first_name = user_info.first_name

    if user_info is None:
        return redirect("login")

    if user_info.is_admin:
        return render(request, "admin/admin.html", {"user_info":user_info, "first_name":first_name})

    elif user_info.is_homeroom:
        return render(request, "hrteacher/hrTeacher.html", {"user_info":user_info, "first_name":first_name})

    elif user_info.is_teacher:
        return render(request, "user/user.html", {"user_info": user_info, "first_name":first_name})

@staff_member_required
def teacher_data_view(request):
    objects = Teacher.objects.all()

    count = objects.count()

    return render(request, "admin/teacher.html", {"teachers": objects, "count":range(1, count + 1)})

@staff_member_required
def add_teacher_view(request):
    get = request.POST.get
    if request.method == "POST":
        uid = get('uid')
        first_name = get('first_name')
        last_name = get('last_name')
        password = get('password')
        email = get('email')
        gender = get('gender')
        status = get('level')
        course = get('course')

        user = ThearningUser.objects.create(
            uid=uid,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            status=status,
        )

        teacher = Teacher.objects.create(user=user, course_id=course)

        user.save()
        teacher.save()

    return render(request, "admin/addTeacher.html")
    

def students_list(request):

    students = Student.objects.all()

    return render(request, "admin/student.html",{"students":students})

# UNIMPLEMENTED VIEWS

def class_view(request):
    return render(request, "admin/class.html")

def course_view(request):
    return render(request, "admin/course.html")

def report_view(request):
    return render(request, "admin/report.html")

def history_view(request):
    return render(request, "admin/history.html")


