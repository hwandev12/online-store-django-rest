# Generated by Django 3.2 on 2023-07-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_sellerprofile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_developer',
            field=models.BooleanField(default=False),
        ),
    ]
