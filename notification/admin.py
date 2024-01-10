from django.contrib import admin
from .models import Notification, Blog, Reaction
# Register your models here.

admin.site.register(Blog)
admin.site.register(Notification)