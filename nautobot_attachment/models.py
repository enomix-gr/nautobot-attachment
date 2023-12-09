# models.py
from django.db import models

from nautobot.apps.models import BaseModel
from nautobot.dcim.models import Location

import os

class Attachment(BaseModel):
    """Base model for attachments."""

    # name = models.CharField(max_length=50)
    file = models.FileField(upload_to="generic-attachments")
    parent = models.ForeignKey(Location, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.file.name)

