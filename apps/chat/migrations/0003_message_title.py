# Generated by Django 4.2.1 on 2023-06-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]