from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Mqtt(models.Model):
    msg = models.TextField()
    topic = models.CharField(max_length=180,default=" ")
    time = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.msg

class Gps(models.Model):
    lat = models.CharField(max_length=500,blank=True)
    lng = models.CharField(max_length=500,blank=True)
    speed = models.CharField(max_length=500,blank=True)
    time = models.DateTimeField(auto_now=False,auto_now_add=True)
    deviceId = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.deviceId

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    mobile_no = models.CharField(max_length=20, default="+91")
    date_of_birth = models.DateField(default=timezone.now())
    gender_choice = (
        ('M', 'Male'), ('F', 'Female')
    )
    gender = models.CharField(max_length=10, choices=gender_choice, default='M')
    profilePic = models.FileField(upload_to='profile/', blank=False, default='img/avatar5.png')
    verificationCode = models.CharField(max_length=250, default='zxsaqw')

    def __str__(self):
        return self.user.username

