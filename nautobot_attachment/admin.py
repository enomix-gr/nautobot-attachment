# admin.py
from django.contrib import admin
from nautobot.apps.admin import NautobotModelAdmin

from .models import Attachment


@admin.register(Attachment)
class Attachment(NautobotModelAdmin):
    list_display = ('created', 'parent', 'file')
