# Generated by Django 2.2.4 on 2019-08-21 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0013_auto_20190821_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[('TEXT', 'TEXT'), ('LONG_TEXT', 'LONG_TEXT'), ('DATE', 'DATE'), ('DATETIME', 'DATETIME'), ('CHECK_BOX', 'CHECK_BOX'), ('MULTICHOICE', 'MULTICHOICE'), ('FILE', 'FILE')], default='TEXT', max_length=20),
        ),
    ]
