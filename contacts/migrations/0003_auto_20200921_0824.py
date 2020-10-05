# Generated by Django 2.2 on 2020-09-21 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200917_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]