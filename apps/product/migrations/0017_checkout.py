# Generated by Django 4.2.1 on 2023-06-21 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0016_alter_ratingproduct_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(default=998)),
                ('email', models.EmailField(max_length=254)),
                ('post_office', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(choices=[('Tashkent', 'Tashkent'), ('Samarkand', 'Samarkand'), ('Bukhara', 'Bukhara'), ('Khiva', 'Khiva'), ('Nukus', 'Nukus'), ('Andijan', 'Andijan'), ('Namangan', 'Namangan'), ('Fergana', 'Fergana'), ('Navoi', 'Navoi'), ('Urgench', 'Urgench'), ('Termez', 'Termez'), ('Kokand', 'Kokand')], default='Tashkent', max_length=200)),
                ('house', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField(default=156876)),
                ('message', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
            },
        ),
    ]
