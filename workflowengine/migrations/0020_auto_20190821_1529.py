# Generated by Django 2.2.4 on 2019-08-21 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflowengine', '0019_formdata'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flow',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='formdata',
            name='flow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='workflowengine.Flow'),
        ),
        migrations.AlterField(
            model_name='form',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='river.State'),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='text',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]