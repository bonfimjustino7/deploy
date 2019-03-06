from django.db import models

# Create your models here.
class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	dt_criacao = models.DateTimeField(auto_now_add=True)

