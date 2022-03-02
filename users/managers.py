from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class ThearningUserManager(BaseUserManager):

    def create_user(self, uid, password, **extra_fields):

        if not uid:
            raise ValueError(_('The UID must be set'))

        user = self.model(uid=uid, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, uid, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', "admin")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('status') is not "admin":
            raise ValueError(_('Admin must have status=admin.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(uid, password, **extra_fields)


