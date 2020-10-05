# Generated by Django 2.2 on 2020-09-17 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 17, 14, 46, 25, 876064, tzinfo=utc)),
        ),
    ]
