# Generated by Django 4.1.4 on 2023-01-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(choices=[('enduro', 'enduro'), ('street', 'street')], default='Cualquiera', max_length=50),
        ),
    ]
