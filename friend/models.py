from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django_project.settings import AUTH_USER_MODEL


class Friend(models.Model):

    status = models.CharField(max_length=10)
    from_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'from_user')
    to_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="to_user")
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.to_user.email

