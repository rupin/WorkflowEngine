# Generated by Django 2.2.4 on 2019-08-18 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0005_auto_20190818_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('field', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Field')),
                ('form', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='workflowengine.Form')),
            ],
        ),
    ]
