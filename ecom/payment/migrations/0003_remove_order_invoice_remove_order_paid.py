# Generated by Django 4.2.17 on 2025-01-11 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_invoice_order_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='invoice',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
    ]
