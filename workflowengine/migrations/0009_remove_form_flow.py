# Generated by Django 2.2.4 on 2019-08-20 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0008_userrole_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='flow',
        ),
    ]