from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(Notification)
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(Subscription)
admin.site.register(Comment)