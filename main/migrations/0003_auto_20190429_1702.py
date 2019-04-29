# Generated by Django 2.2 on 2019-04-29 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190421_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='downtown',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='attending',
            field=models.ManyToManyField(to='main.Downtown'),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]