from django.urls import path, include

from .views import dashboard, teacher_data

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('teacher', teacher_data, name="teacher")
]