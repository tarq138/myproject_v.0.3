# Generated by Django 2.0.2 on 2018-03-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_floors'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='height',
            field=models.DecimalField(decimal_places=2, default=2.8, max_digits=4),
        ),
        migrations.AddField(
            model_name='product',
            name='rooms',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=2),
        ),
    ]
