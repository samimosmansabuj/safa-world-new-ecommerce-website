# Generated by Django 5.0 on 2023-12-11 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('phone_number', models.CharField(max_length=14)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='customer/profile_pic/')),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('Shipping Address', 'Shipping Address'), ('Billing Address', 'Billing Address'), ('Address', 'Address')], default='Address', max_length=50)),
                ('address', models.CharField(blank=True, max_length=600, null=True)),
                ('upazila', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('post_code', models.CharField(blank=True, max_length=4, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.customer')),
            ],
            options={
                'ordering': ['updated_date'],
            },
        ),
    ]
