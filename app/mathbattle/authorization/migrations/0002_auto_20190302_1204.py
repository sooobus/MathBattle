# Generated by Django 2.1.5 on 2019-03-02 09:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 9, 4, 43, 151025, tzinfo=utc)),
        ),
    ]
