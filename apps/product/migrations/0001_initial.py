# Generated by Django 4.2.3 on 2023-07-20 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_user_is_developer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('product_name', models.CharField(max_length=200)),
                ('product_cost', models.IntegerField(blank=True, default=0, null=True)),
                ('product_quantity', models.IntegerField()),
                ('product_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('product_status', models.BooleanField(default=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Product Category',
                'verbose_name_plural': 'Product Category',
            },
        ),
        migrations.CreateModel(
            name='RatingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rating Product',
                'verbose_name_plural': 'Rating Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(upload_to='products/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='product.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_product', to='authentication.selleraccountmodel'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='CheckoutItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.buyeraccountmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.IntegerField(default=62952735, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
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
                ('checkout_items', models.ManyToManyField(to='product.checkoutitem')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.buyeraccountmodel')),
            ],
            options={
                'verbose_name': 'Checkout',
                'verbose_name_plural': 'Checkouts',
            },
        ),
    ]
