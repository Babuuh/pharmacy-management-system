# Generated by Django 3.1.7 on 2021-05-04 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_remove_invoice_invoice_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='exipry_date',
            field=models.DateField(),
        ),
    ]
