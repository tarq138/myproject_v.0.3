# Generated by Django 2.0.2 on 2018-03-04 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20180305_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='water_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
