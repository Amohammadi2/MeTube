from django.contrib import admin
from django import forms
from .models import *
# Register your models here

class VideoFormAdmin(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Video
        exclude = []

class VideoAdmin(admin.ModelAdmin):
    form = VideoFormAdmin

def register_models():
    admin.site.register(Profile)
    admin.site.register(Notification)
    admin.site.register(Channel)
    admin.site.register(Video, VideoAdmin)
    admin.site.register(Subscription)
    admin.site.register(Comment)

register_models()