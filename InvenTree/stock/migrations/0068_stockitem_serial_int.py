# Generated by Django 3.2.5 on 2021-11-09 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0067_alter_stockitem_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='serial_int',
            field=models.IntegerField(default=0),
        ),
    ]