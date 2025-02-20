from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f' {self.id} - {self.nome}'
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    data_pedido = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f' Pedido: {self.id} Cliente: {self.cliente.nome}  {self.data_pedido} '

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade} {self.produto} (Pedido {self.pedido.id})'