# Generated by Django 2.2.4 on 2019-08-21 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0018_auto_20190821_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('text', models.CharField(default='', max_length=500, null=True)),
                ('formfield', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workflowengine.FormField')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]