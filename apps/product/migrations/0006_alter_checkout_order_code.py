# Generated by Django 3.2 on 2023-07-07 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_checkout_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='order_code',
            field=models.IntegerField(default=58677573, null=True),
        ),
    ]
