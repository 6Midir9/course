# Generated by Django 5.0.4 on 2024-04-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contact',
            field=models.CharField(max_length=200, verbose_name='Контакти'),
        ),
    ]
