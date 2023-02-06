# Generated by Django 4.1.4 on 2023-01-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0006_alter_product_style'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.IntegerField(verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(choices=[('Offroad', 'Offroad'), ('Street', 'Street'), ('Scooter', 'Scooter')], max_length=50, verbose_name='Estilo'),
        ),
    ]
