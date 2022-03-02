from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from users.models import ThearningUser


class ThearningAuthBackend(BaseBackend):

    def authenticate(self, request, uid=None, password=None):

        try:
            customer = ThearningUser.objects.get(uid=uid)
            if customer.user.check_password(password) is True:
                return customer.user
        except ThearningUser.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        try:
            return ThearningUser.objects.get(pk=user_id)
        except ThearningUser.DoesNotExist:
            return None