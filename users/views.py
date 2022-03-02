from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .models import ThearningUser

def login_view(request):
    # if request.method == "POST":
    #     uid = request.POST.get("uid")
    #     _user = ThearningUser.objects.filter(user__userinfo__uid=uid).first()
    #     password = request.POST.get("password")
    #     user = authenticate(request, username=_user.user.username, password=password)
    #     if user:
    #         login(request, user)
    #         return HttpResponseRedirect(reverse('dashboard'))
    #     else:
    #         return HttpResponse('Invalid login details!')
    #
    # return render(request, "login.html")
    pass

@login_required
def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('login'))


