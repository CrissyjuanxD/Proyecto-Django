# Generated by Django 4.2 on 2024-05-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer_invoice_product_cost_product_iva_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='categorys/default.png', null=True, upload_to='categorys/'),
        ),
    ]
