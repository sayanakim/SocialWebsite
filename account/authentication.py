from django.contrib.auth.models import User

class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, used_id):
        try:
            return User.objects.get(pk=used_id)
        except User.DoesNotExist:
            return None
