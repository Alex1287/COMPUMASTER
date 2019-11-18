from django.contrib import admin
#from .models import Empleado, Usuario, Cliente, Costo, Equipo, Garantia, Orden, , Rol, DetalleProducto
from .models import Producto, Empleado, Usuario, Cliente, Orden, Garantia, Venta

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Venta)
#admin.site.register(Equipo)
admin.site.register(Garantia)
admin.site.register(Orden)
admin.site.register(Producto)
#admin.site.register(Rol)
#admin.site.register(DetalleProducto)
