from nautobot.apps import NautobotAppConfig

class NautobotAttachmentConfig(NautobotAppConfig):
    name = 'nautobot_attachment'
    verbose_name = 'Attachments for Nautobot'
    description = 'Adds attachments to any nautobot content-type'
    version = '0.1'
    author = 'Alexis Panagiotopoulos'
    author_email = 'apanagio@enomix.gr'
    base_url = 'attachments'
    required_settings = []
    default_settings = {
        'content-types': ['dcim.location']
    }

config = NautobotAttachmentConfig