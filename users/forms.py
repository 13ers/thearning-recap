from django import forms

from .models import Teacher, ThearningUser


# class ThearningUserForm(forms.Form):
#     uid = forms.CharField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.CharField()
#     gender = forms.CharField()
#     course = forms.ChoiceField(choices=(
#         (1, "Bahasa Indonesia"),
#         (2, "Matematika"),
#         (3, "Bahasa Inggris"),
#
#     ))

class ThearningUserForm(forms.ModelForm):

    class Meta:
        model = ThearningUser
        fields = (
            "uid",
            "first_name",
            "last_name",
            "email",
            "gender",
        )

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ("course",)
