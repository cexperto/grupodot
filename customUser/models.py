from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # author_pseudonym = models.CharField(max_length=200)
    able = models.IntegerField(default=1)