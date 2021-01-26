# Generated by Django 2.1.2 on 2019-02-28 09:04

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contest_page', '0006_auto_20190228_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='dateED',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 28, 9, 4, 0, 849695, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='dateST',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 28, 9, 4, 0, 849646, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='tasks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=[], size=None),
        ),
    ]
