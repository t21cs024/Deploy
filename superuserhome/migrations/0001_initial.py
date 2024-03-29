# Generated by Django 4.1.7 on 2024-01-19 10:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import superuserhome.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('company_address', models.CharField(blank=True, max_length=100)),
                ('company_mail', models.EmailField(max_length=254)),
                ('company_phone_number', models.CharField(max_length=15)),
                ('manager_name', models.CharField(blank=True, max_length=50)),
                ('manager_phone_number', models.CharField(max_length=15)),
                ('manager_mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to=superuserhome.models.savePath)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=100)),
                ('state', models.CharField(choices=[('in stock', '在庫あり'), ('sold out', '売り切れ'), ('ordered', '発注済み'), ('2', '非買商品')], default='in stock', max_length=10)),
                ('ishalf', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_month', models.PositiveIntegerField(default=1)),
                ('buy_amount', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_weight', models.DecimalField(decimal_places=2, default=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(2.0)])),
                ('order_quantity', models.PositiveIntegerField(default=50)),
                ('minimum_amount', models.PositiveIntegerField(default=10)),
                ('last_sold_out_date', models.DateField(blank=True, null=True)),
                ('item', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='superuserhome.item')),
            ],
        ),
        migrations.CreateModel(
            name='BuyHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('buy_date', models.DateField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='superuserhome.item')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
