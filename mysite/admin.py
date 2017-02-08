from django.contrib import admin
from .models import Mqtt,Gps

from . models import Account

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Account)
admin.site.register(Mqtt)

admin.site.register(Gps)


# Define an inline console descriptor for Employee model
# which acts a bit like a singleton
class Accountsinline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts Model'

# Define a new User console
class UserAdmin(BaseUserAdmin):
    inlines = (Accountsinline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)