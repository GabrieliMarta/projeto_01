from django.contrib import admin

from .models import Cliente
from .models import Pedido
from .models import ItensPedido

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
