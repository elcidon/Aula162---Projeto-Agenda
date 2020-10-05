# Generated by Django 2.2 on 2020-09-17 14:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 9, 17, 14, 16, 36, 160634, tzinfo=utc))),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.Category')),
            ],
        ),
    ]
