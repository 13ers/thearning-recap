from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from django.urls import reverse

from users.models import UserInfo

def dashboard(request):

    try:
        user_info = UserInfo.objects.filter(user__username=request.user).first()
    except User.DoesNotExist:
        user_info = None

    if user_info is None:
        return redirect("login")

    if user_info.status == "admin":
        return render(request, "admin.html")

    elif user_info.status == "homeroom":
        return render(request, "hrTeacher.html")

    elif user_info.status == "teacher":
        return render(request, "user.html")

@staff_member_required
def teacher_data(request):
    return render(request, "teacher.html")

