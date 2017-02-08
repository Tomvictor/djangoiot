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
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, primary_key=True)
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

class Device(models.Model):
    account = models.ManyToManyField(Account)
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name

class DeviceStatus(models.Model):
    device = models.ForeignKey(Device)
    range_choice = (
        ('In','InRange'), ('Out','OutOfRange')
    )
    range = models.CharField(max_length=50, choices=range_choice, default='In')
    battery_state = models.IntegerField(blank=True)
    raw_gps = models.TextField(blank=True)
    latitude = models.CharField(max_length=150, blank=True)
    longitude = models.CharField(max_length=150, blank=True)
    status_choice = (
        ('Online', 'Online'), ('Offline', 'Offline')
    )
    status = models.CharField(max_length=50, choices=status_choice, default='Online')
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.range
