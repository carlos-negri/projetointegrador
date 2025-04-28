from django.db import models

from clientes.models import Cliente


class Visita(models.Model):
    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Linka ao cliente
    # corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE)  # Linka ao corretor
    # data_hora = models.DateTimeField()  # Data e hora da visita
    # observacoes = models.TextField(blank=True)  # Campo opcional

    def __str__(self):
        return f"Visita em {self.imovel} por {self.cliente}"