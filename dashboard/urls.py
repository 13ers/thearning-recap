from django.urls import path, include

# from .views import dashboard_view, teacher_data_view, students_list, add_teacher_view
from .views import *

urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('teacher', teacher_data_view, name="teacher"),
    path("teacher/add", add_teacher_view, name="addteacher"),
    path('students', students_list, name="student"),
    path("class", class_view, name="class"),
    path("course", course_view, name="course"),
    path("report", report_view, name="report"),
    path("history", history_view, name="history"),
]