from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == "POST":
        uid = request.POST.get("uid")
        password = request.POST.get("password")
        user = authenticate(request, username=uid, password=password)

        if user:
            login(request, user)
        else:
            return HttpResponseRedirect("login")
    
    return render(request, "login.html")


