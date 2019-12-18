from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.apps import apps
from django.contrib.auth import get_user_model

userModel = get_user_model()

class UserAccountBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return userModel.objects.get(id=user_id)
        except userModel.DoesNotExist:
            return None