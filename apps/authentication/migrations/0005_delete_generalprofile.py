# Generated by Django 4.2.1 on 2023-06-06 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_buyerprofile_user_alter_sellerprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeneralProfile',
        ),
    ]
