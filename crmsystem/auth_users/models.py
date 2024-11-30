from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50,)
    full_name = models.CharField(max_length=50,)

