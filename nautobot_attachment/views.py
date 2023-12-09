from nautobot.core.views.generic import ObjectDeleteView
from nautobot.dcim.models import Location

from django.views.generic import View
from django.http import HttpResponse
from django.core.exceptions import BadRequest

from .models import Attachment

class AttachmentDeleteView(ObjectDeleteView):
    """ Delet attachment object """
    queryset = Attachment.objects.all()

    def get_return_url(self, request, imageattachment):
        return imageattachment.parent.get_absolute_url()


class AttachmentAddView(View):
    """ Add an attachment to the given object """

    def post(self, request, pk):
        parent = Location.objects.get(pk=pk)
        att = Attachment(parent=parent, file=request.FILES["file1"])

        # raise BadRequest('Invalid request.')
        att.save()
        return HttpResponse(f"Hello, World!{pk}")

