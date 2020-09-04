# Generated by Django 2.2.12 on 2020-06-05 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_invoice_bill_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Created: Waiting for billing'), (1, 'Billed: Waiting for payment'), (2, 'Rejected: Denied payment within 30 days'), (3, 'Paid: Received payment')], default=0),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='description',
            field=models.CharField(max_length=96),
        ),
    ]