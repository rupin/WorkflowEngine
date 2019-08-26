# Generated by Django 2.2.4 on 2019-08-26 05:14

from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    dependencies = [
        ('river', '0001_initial'),
        ('workflowengine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flow',
            name='stage',
            field=river.models.fields.state.StateField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.State'),
        ),
        migrations.AddField(
            model_name='form',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='river.State'),
        ),
        migrations.AddField(
            model_name='formfield',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='river.State'),
        ),
    ]