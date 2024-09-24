from django.db import models


class Roll(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    prezzo = models.FloatField()
    
    def __str__(self):
        return self.nome
