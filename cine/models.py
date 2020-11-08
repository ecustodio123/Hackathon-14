from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genero(models.Model):
    STATUS = (
        (0, 'No disponible'),
        (1, 'Disponible')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, blank=False, null=False)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['id']
        indexes = [
            models.Index(fields=['name', 'status'])
        ]

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    STATUS = (
        (0, 'No disponible'),
        (1, 'Disponible')
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='images/posts', max_length=255, blank=True, null=True)
    resumen = models.TextField(blank=False, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, blank=False, null=False)
    release_date = models.DateField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'
        ordering = ['id']
        indexes = [
            models.Index(fields=['title', 'slug', 'genero', 'user', 'status'])
        ]
    
    def __str__(self):
        return self.title

class Local(models.Model):
    STATUS = (
        (0, 'Cerrado'),
        (1, 'Abierto')
    )

    id = models.AutoField(primary_key=True)
    local = models.CharField(max_length=120, blank=False, null=False)
    slug_local = models.SlugField(max_length=255, blank=False, null=False)
    image_local = models.ImageField(upload_to='images/posts', max_length=255, blank=True, null=True)
    status = models.IntegerField(default=1, choices=STATUS)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
        ordering = ['id']
        indexes = [
            models.Index(fields=['local', 'status'])
        ]

    def __str__(self):
        return self.local

class Cartelera(models.Model):
    STATUS = (
        (0, 'No disponible'),
        (1, 'Disponible')
    )

    id = models.AutoField(primary_key=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, blank=False, null=False)
    slug = models.SlugField(max_length=255, blank=False, null=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=False, null=False)
    horario = models.TimeField(blank=False,null=False)
    num_asientos = models.IntegerField(blank=False, null=False)
    status = models.IntegerField(default=1, choices=STATUS)
    
    class Meta:
        verbose_name = 'Cartelera'
        verbose_name_plural = 'Carteleras'
        ordering = ['id']
        indexes = [
            models.Index(fields=['pelicula', 'local', 'horario', 'status'])
        ]

    def __int__(self):
        return self.num_asientos

class Compra(models.Model):
    STATUS = (
        (0, 'Inactivo'),
        (1, 'Activo')
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, blank=False, null=False)
    num_tickets = models.IntegerField(default=1, blank=False, null=False)
    precio_pagar = models.IntegerField(default=20, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, blank=False, null=False)
    published_date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=1, choices=STATUS)
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['id']
        indexes = [
            models.Index(fields=['pelicula', 'num_tickets', 'precio_pagar', 'content', 'local'])
        ]

    def __str__(self):
        return f'{self.pelicula.title}  - {self.user.username}'

