from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, unique=True)
    avatar = models.ImageField(upload_to=f'avatars/%d/%m/%S/{phone}', null=True, blank=True)

    objects = UserManager()
    #USERNAME_FIELD = 'phone'
