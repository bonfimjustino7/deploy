from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Categoria(models.Model):
	nome = models.CharField(max_length=100)
	dt_criacao = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.nome

	class Meta:
		permissions = (
            ("add_cat", "Can change the status of task"),
            ("del_cat", "Can remove a task by setting its status as closed"),
        )

class Pedido(models.Model):
	pedido = models.CharField(max_length=200)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	data = models.DateTimeField()

	def __str__(self):
		return self.pedido
	
	class Meta:
		permissions = (
            ("add_ped", "pode add pedido"),
            ("del_ped", "pode excluir pedido"),
        )
