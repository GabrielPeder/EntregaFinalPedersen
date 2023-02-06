from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Nombre')
    image = models.ImageField(upload_to='categories', verbose_name='Imagen')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'