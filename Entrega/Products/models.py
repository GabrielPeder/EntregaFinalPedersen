from django.db import models

class Product(models.Model):
    STYLE_CHOICES = (
        ('Offroad', 'Offroad'),
        ('Street', 'Street'),
        ('Scooter', 'Scooter'),
    )

    name = models.CharField(max_length=100, verbose_name = 'Nombre')
    model = models.IntegerField(verbose_name = 'Modelo')
    style = models.CharField(max_length=50, choices=STYLE_CHOICES, verbose_name = 'Estilo')
    price = models.FloatField(verbose_name = 'Precio')
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', verbose_name='Imagen', null=True, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
