# template_content.py
from django.urls import reverse
from nautobot.apps.ui import TemplateExtension

from .models import Attachment


class LocationAttachment(TemplateExtension):
    """Template extension to display the attachments of the current location"""

    model = 'dcim.location'

    def right_page(self):
        return self.render('nautobot_attachment/attachments.html', extra_context={
            # "attachments": Attachment.objects.filter(location=self.context['object'].pk)
            "attachments": self.context['object'].attachment_set.all()
        })


template_extensions = [LocationAttachment]
