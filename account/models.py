from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField("Email Address", unique=True)
    phone_number = models.CharField("Phone Number", max_length=13)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)

