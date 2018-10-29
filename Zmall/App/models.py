from django.db import models

# Create your models here.


class UserT(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
    tel = models.CharField(max_length=20)


