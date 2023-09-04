from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=1000, default='')
    lname = models.CharField(max_length=1000, default='')
    email = models.CharField(max_length=1000, default='')
    contact = models.CharField(max_length=1000, default='')
    password = models.CharField(max_length=1000, default='')
    accountInfo = models.CharField(max_length=50000, default='')

    def __str__(self):
        return self.fname + ' ' + self.lname + ' - ' + self.email

class ServiceRecords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=1000, default='', null=True, blank=True)
    email = models.CharField(max_length=1000, default='', null=True, blank=True)
    password = models.CharField(max_length=1000, default='', null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.email + ' - ' + self.service