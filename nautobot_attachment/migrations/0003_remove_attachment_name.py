# Generated by Django 3.2.23 on 2023-11-19 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_attachment', '0002_rename_animal_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='name',
        ),
    ]