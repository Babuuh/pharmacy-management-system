# Generated by Django 3.1.7 on 2021-05-04 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_invoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_no',
        ),
    ]