# Generated by Django 2.1.5 on 2019-02-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='test', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='test', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='test', max_length=200),
        ),
    ]