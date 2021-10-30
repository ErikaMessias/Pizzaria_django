from django.db import models

class Pizzaria(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True,upload_to='fotos/%y/%m/%d/')

    def __str__(self):
        return self.titulo
