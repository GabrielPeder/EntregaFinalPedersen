from django.db import models

class Provider(models.Model):
    CONDITION_CHOICES = (
        ('monotributista', 'monotributista'),
        ('responsable inscripto', 'responsable inscripto'),
    )

    name = models.CharField(max_length=100, verbose_name = 'Nombre')
    address = models.CharField(max_length=300, verbose_name = 'Dirección')
    phone_number = models.CharField(max_length=20, verbose_name = 'Teléfono')
    email = models.EmailField()
    condition = models.CharField(max_length=50, choices = CONDITION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.email}' 

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'