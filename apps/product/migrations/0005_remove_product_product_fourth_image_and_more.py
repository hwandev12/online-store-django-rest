# Generated by Django 4.2.1 on 2023-06-15 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_product_fourth_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_fourth_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_second_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_third_image',
        ),
    ]
