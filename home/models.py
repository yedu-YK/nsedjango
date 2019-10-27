from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)

class SuperAdmin(models.Model):
    admin_name = models.CharField(max_length=20, blank=False, null=False)
    admin_password = models.CharField(max_length=20, blank=False, null=False)

