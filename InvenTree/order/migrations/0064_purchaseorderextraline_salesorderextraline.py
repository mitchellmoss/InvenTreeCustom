# Generated by Django 3.2.12 on 2022-03-27 01:11

import InvenTree.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0063_alter_purchaseorderlineitem_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrderExtraLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', InvenTree.fields.RoundingDecimalField(decimal_places=5, default=1, help_text='Item quantity', max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity')),
                ('reference', models.CharField(blank=True, help_text='Line item reference', max_length=100, verbose_name='Reference')),
                ('notes', models.CharField(blank=True, help_text='Line item notes', max_length=500, verbose_name='Notes')),
                ('target_date', models.DateField(blank=True, help_text='Target shipping date for this line item', null=True, verbose_name='Target Date')),
                ('context', models.JSONField(blank=True, help_text='Additional context for this line', null=True, verbose_name='Context')),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('price', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=4, default_currency='', help_text='Unit price', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Price')),
                ('order', models.ForeignKey(help_text='Sales Order', on_delete=django.db.models.deletion.CASCADE, related_name='extra_lines', to='order.salesorder', verbose_name='Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderExtraLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', InvenTree.fields.RoundingDecimalField(decimal_places=5, default=1, help_text='Item quantity', max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity')),
                ('reference', models.CharField(blank=True, help_text='Line item reference', max_length=100, verbose_name='Reference')),
                ('notes', models.CharField(blank=True, help_text='Line item notes', max_length=500, verbose_name='Notes')),
                ('target_date', models.DateField(blank=True, help_text='Target shipping date for this line item', null=True, verbose_name='Target Date')),
                ('context', models.JSONField(blank=True, help_text='Additional context for this line', null=True, verbose_name='Context')),
                ('price_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('price', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=4, default_currency='', help_text='Unit price', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Price')),
                ('order', models.ForeignKey(help_text='Purchase Order', on_delete=django.db.models.deletion.CASCADE, related_name='extra_lines', to='order.purchaseorder', verbose_name='Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
