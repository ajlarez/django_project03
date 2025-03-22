from django.db import models

# Create your models here.




class Movies(models.Model):
    pass

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField(blank=True, null=True)
    anio_estreno = models.IntegerField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True, help_text="Duración en minutos")
    generos = models.CharField(max_length=100, default='Drama')
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)
    puntuacion = models.FloatField(blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)
    actores = models.TextField(blank=True, null=True, help_text="Lista de actores separados por comas")

    def __str__(self):
        return self.titulo