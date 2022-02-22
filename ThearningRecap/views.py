from django.http import HttpResponseRedirect

def index():
    return HttpResponseRedirect("login")