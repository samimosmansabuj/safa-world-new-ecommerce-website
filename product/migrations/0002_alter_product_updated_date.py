# Generated by Django 5.0 on 2023-12-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
