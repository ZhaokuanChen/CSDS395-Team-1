# Generated by Django 4.0.4 on 2022-04-23 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
