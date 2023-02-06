from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name = 'Usuario' )
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name = 'Teléfono')
    birth_date = models.DateField(null=True, blank=True, verbose_name = 'Fecha de Nacimiento')
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True, verbose_name = 'Imagen de Perfil')