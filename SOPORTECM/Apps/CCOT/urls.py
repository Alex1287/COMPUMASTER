"""SOPORTECM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import OrdenesView, VordenesView, GarantiasView, VgarantiasView, EordenesView, EgarantiasView, CclienteView, GclienteView, RegistroView, orden_print, ordenes_print, garantia_print, garantias_print, productos_print, ventas_print, venta_print
#from .views import ProductosView, VordenesView, VgarantiasView, VproductosView
from .views import IndexView, HomeView, AcercaView, ProductosView, VproductosView, EmpleadoView, VempleadosView, UsuarioView, VusuarioView, EusuarioView, DusuarioView, EproductosView, ClienteView, VclienteView, EclienteView, EempleadosView, AusuarioView, VentaView, VventaView, EventaView
#from .views import CrearUsuarioView, CrearEmpleado, ProductosView
#from django.views.generic.edit import CrearEmpleado

app_name = 'CCOT'
urlpatterns = [

    #path('', IndexView.as_view(), name='index'),
    path('', HomeView.as_view(), name='home'),
    path('IngresarOrdenes', OrdenesView.as_view(), name='ordenes'),
    path('CrearClientesOrdenes', CclienteView.as_view(), name='occlientes'),
    path('VerOrdenes', VordenesView.as_view(), name='vordenes'),
    path('EditarOrdenes/<int:pk>', EordenesView.as_view(), name='eordenes'),
    path('IngresarGarantias', GarantiasView.as_view(), name='garantias'),
    path('CrearClientesGarantias', GclienteView.as_view(), name='gcclientes'),
    path('VerGarantias', VgarantiasView.as_view(), name='vgarantias'),
    path('EditarGarantias/<int:pk>', EgarantiasView.as_view(), name='egarantias'),
    path('IngresarProductos', ProductosView.as_view(), name='productos'),
    path('VerProductos', VproductosView.as_view(), name='vproductos'),
    path('Acerca', AcercaView.as_view(), name='acerca'),
    path('EditarProductos/<int:pk>', EproductosView.as_view(), name='eproductos'),
    path('IngresarEmpleados', EmpleadoView.as_view(), name='cempleados'),
    path('VerEmpleados', VempleadosView.as_view(), name='vempleados'),
    path('EditarEmpleados/<int:pk>', EempleadosView.as_view(), name='eempleados'),
    path('CrearUsuarios', UsuarioView.as_view(), name='cusuarios'),
    path('VerUsuarios', VusuarioView.as_view(), name='vusuarios'),
    path('EditarUsuarios/<int:pk>', EusuarioView.as_view(), name='eusuarios'),
    path('EliminarUsuarios/<int:pk>', DusuarioView.as_view(), name='dusuarios'),
    path('ActivarUsuarios/<int:pk>', AusuarioView.as_view(), name='ausuarios'),
    path('ActivarUsuarios/<int:pk>', RegistroView.as_view(), name='ausuarios'),
    path('CrearClientes', ClienteView.as_view(), name='cclientes'),
    path('VerClientes', VclienteView.as_view(), name='vclientes'),
    path('EditarClientes/<int:pk>', EclienteView.as_view(), name='eclientes'),
    path('VentaProductos', VentaView.as_view(), name='ventas'),
    path('VerVentas', VventaView.as_view(), name='vventas'),
    path('EditarVentas/<int:pk>', EventaView.as_view(), name='eventas'),
    path('RegistrarUsuario', RegistroView.as_view(), name='rusuarios'),
    path('Ordenes/print', ordenes_print, name='ordenes_print'),
    path('Ordenes/print/<int:pk>', orden_print, name='orden_print_one'),
    path('Garantias/print', garantias_print, name='garantias_print'),
    path('Garantias/print/<int:pk>', garantia_print, name='garantia_print_one'),
    path('Productos/print', productos_print, name='productos_print'),
    path('Ventas/print', ventas_print, name='ventas_print'),
    path('Ventas/print/<int:pk>', venta_print, name='venta_print_one'),
]
