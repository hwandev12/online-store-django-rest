# Generated by Django 4.2.1 on 2023-06-17 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_productcategory_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Category'},
        ),
    ]
