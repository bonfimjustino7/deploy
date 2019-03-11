from django.db import models

# Create your models here.
class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	dt_criacao = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nome

class Pedido(models.Model):
	pedido = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	data = models.DateTimeField()

	def __str__(self):
		return self.pedido
