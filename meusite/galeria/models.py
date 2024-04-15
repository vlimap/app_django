from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    opcoes_categorias = [
        ("nebulosa","nebulosa"),
        ("estrela","estrela"),
        ("galaxia","galaxia"),
        ("planeta","planeta"),
    ]
    nome = models.CharField(max_length = 100, null = False, blank = False)
    legenda = models.CharField(max_length = 150, null = False, blank = False)
    categoria = models.CharField(max_length = 100, choices = opcoes_categorias, default='')
    descricao = models.TextField(null = False, blank = False)
    foto = models.ImageField(upload_to = "fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return  self.nome



