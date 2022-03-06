# from django import forms
# from django.contrib import admin
# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.core.exceptions import ValidationError
#
# from dashboard.models import ThearningUser
#
#
# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = ThearningUser
#         fields = '__all__'
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = ThearningUser
#         fields = '__all__'
#
#
# class UserAdmin(BaseUserAdmin):
#
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     list_display = '__all__',
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('uid', 'email', 'password')}),
#         ('Personal info', {'fields': ('fullname', 'gender', 'date_joined')}),
#         ('Permissions', {'fields': ('status',)}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': '__all__',
#         }),
#     )
#     search_fields = ('uid', 'email')
#     ordering = ('uid',)
#     filter_horizontal = ()
#
#
# # Now register the new UserAdmin...
# admin.site.register(ThearningUser, UserAdmin)
# # ... and, since we're not using Django's built-in permissions,
# # unregister the Group model from admin.
# admin.site.unregister(Group)