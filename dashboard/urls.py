from django.urls import path, include

from .views import dashboard_view, teacher_data_view, students_list, add_teacher_view

urlpatterns = [
    path('', dashboard_view, name="dashboard"),
    path('teacher', teacher_data_view, name="teacher"),
    path('students', students_list, name="students"),
    path("teacher/add", add_teacher_view, name="addteacher"),
]