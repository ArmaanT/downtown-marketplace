# Generated by Django 2.2 on 2019-04-29 01:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_downtown_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attending',
            field=models.ManyToManyField(to='main.Downtown'),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
