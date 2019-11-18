from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
#from .models import Usuarios
from .models import Producto, Empleado, Usuario, Cliente, Orden, Garantia, Venta
#from django.core.urlresolvers import reverse_lazy
#from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django import forms
from .forms import ProductoForm, EmpleadoForm, UsuarioForm, ClienteForm, OrdenesForm, GarantiasForm, VentaForm, UsuarioEmailForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from datetime import date

from django.contrib.auth.models import User
# Create your views here.

class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self, request, *args, **kwargs):
		return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class IndexView(TemplateView):
			template_name='index.html'

class HomeView(TemplateView):
			template_name='home.html'

@method_decorator(staff_member_required, name = 'dispatch')
class AcercaView(TemplateView):
			template_name='acerca.html'

#class OrdenesView(TemplateView):
#			template_name='ordenes.html'
@method_decorator(staff_member_required, name = 'dispatch')
class OrdenesView(CreateView):
			template_name='ordenes.html'
			form_class = OrdenesForm
			success_url = reverse_lazy('CCOT:vordenes')

@method_decorator(staff_member_required, name = 'dispatch')
class VordenesView(ListView):
			template_name='vordenes.html'
			model = Orden
			paginate_by = 5

			def get_queryset(self):
				return Orden.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EordenesView(UpdateView):
	model = Orden
	form = OrdenesForm
	fields = '__all__'
	template_name = 'eordenes.html'
	success_url = reverse_lazy('CCOT:vordenes')

@method_decorator(staff_member_required, name = 'dispatch')
class GarantiasView(CreateView):
			template_name='garantias.html'
			form_class = GarantiasForm
			success_url = reverse_lazy('CCOT:vgarantias')

@method_decorator(staff_member_required, name = 'dispatch')
class VgarantiasView(ListView):
			template_name='vgarantias.html'
			model = Garantia
			paginate_by = 5

			def get_queryset(self):
				return Garantia.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EgarantiasView(UpdateView):
	model = Garantia
	form = GarantiasForm
	fields = '__all__'
	template_name = 'egarantias.html'
	success_url = reverse_lazy('CCOT:vgarantias')

@method_decorator(staff_member_required, name = 'dispatch')
class ProductosView(CreateView):
	template_name='productos.html'
	form_class = ProductoForm
	#success_url = reverse_lazy('CCOT:vproductos')

	def get_success_url(self):
		return reverse_lazy('CCOT:vproductos') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class VproductosView(ListView):
	template_name='vproductos.html'
	model = Producto
	model = Empleado
	paginate_by = 5

	def get_queryset(self):
		return Producto.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EproductosView(UpdateView):
	model = Producto
	form = ProductoForm
	fields = '__all__'
	template_name = 'eproducto.html'
	success_url = reverse_lazy('CCOT:vproductos')

@method_decorator(staff_member_required, name = 'dispatch')
class EmpleadoView(CreateView):
	template_name='cempleado.html'
	form_class = EmpleadoForm
	#success_url = reverse_lazy('CCOT:vempleados')

	def get_success_url(self):
		return reverse_lazy('CCOT:vempleados') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class VempleadosView(ListView):
	template_name='vempleado.html'
	model = Empleado
	paginate_by = 5

	def get_queryset(self):
		return Empleado.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EempleadosView(UpdateView):
	model = Empleado
	form = EmpleadoForm
	fields = '__all__'
	template_name = 'eempleado.html'
	success_url = reverse_lazy('CCOT:vempleados')

@method_decorator(staff_member_required, name = 'dispatch')
class UsuarioView(CreateView):
			template_name='cusuario.html'
			form_class = UsuarioForm
			success_url = reverse_lazy('CCOT:vusuarios')

@method_decorator(staff_member_required, name = 'dispatch')
class VusuarioView(ListView):
	template_name='vusuario.html'
	model = Usuario
	paginate_by = 5

	def get_queryset(self):
		return Usuario.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EusuarioView(UpdateView):
	model = Usuario
	form = UsuarioForm
	fields = '__all__'
	template_name = 'eusuario.html'
	success_url = reverse_lazy('CCOT:vusuarios')

@method_decorator(staff_member_required, name = 'dispatch')
class AusuarioView(UpdateView):
	model = Usuario
	form = UsuarioForm
	fields = ('activo',)
	template_name = 'ausuario.html'
	success_url = reverse_lazy('CCOT:vusuarios')

@method_decorator(staff_member_required, name = 'dispatch')
class DusuarioView(DeleteView):
	template_name = 'dusuario.html'
	model = Usuario
	form = UsuarioForm
	success_url = reverse_lazy('CCOT:vusuarios')

@method_decorator(staff_member_required, name = 'dispatch')
class ClienteView(CreateView):
	template_name = 'ccliente.html'
	form_class = ClienteForm
	#success_url = reverse_lazy('CCOT:vclientes')

	def get_success_url(self):
		return reverse_lazy('CCOT:vclientes') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class CclienteView(CreateView):
	template_name = 'occliente.html'
	form_class = ClienteForm
	#success_url = reverse_lazy('CCOT:ordenes')

	def get_success_url(self):
		return reverse_lazy('CCOT:ordenes') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class GclienteView(CreateView):
	template_name = 'gccliente.html'
	form_class = ClienteForm
	#success_url = reverse_lazy('CCOT:garantias')

	def get_success_url(self):
		return reverse_lazy('CCOT:garantias') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class VclienteView(ListView):
	template_name='vclientes.html'
	model = Cliente
	paginate_by = 5

	def get_queryset(self):
		return Cliente.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EclienteView(UpdateView):
	model = Cliente
	form = ClienteForm
	fields = '__all__'
	template_name = 'ecliente.html'
	success_url = reverse_lazy('CCOT:vclientes')

@method_decorator(staff_member_required, name = 'dispatch')
class VentaView(CreateView):
	template_name = 'venta.html'
	form_class = VentaForm
	#success_url = reverse_lazy('CCOT:vventas')

	def get_success_url(self):
		return reverse_lazy('CCOT:vventas') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class VventaView(ListView):
	template_name = 'vventa.html'
	model = Venta
	paginate_by = 5

	def get_queryset(self):
		return Venta.objects.all().order_by('-id')

@method_decorator(staff_member_required, name = 'dispatch')
class EventaView(UpdateView):
	model = Venta
	form = VentaForm
	fields = '__all__'
	template_name = 'eventa.html'
	success_url = reverse_lazy('CCOT:vventas')

@method_decorator(staff_member_required, name = 'dispatch')
class RegistroView(CreateView):
	form_class = UsuarioEmailForm
	#success_url = reverse_lazy('CCOT:vusuarios')
	template_name = 'registration/registro.html'

	def get_success_url(self):
		return reverse_lazy('CCOT:vusuarios') + '?register'

@method_decorator(staff_member_required, name = 'dispatch')
class VusuarioView(ListView):
	template_name = 'vusuario.html'
	form_class = User
	paginate_by = 5

	def get_queryset(self):
		return User.objects.all().order_by('-id')

def orden_print(self, pk=None):
   import io
   from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
   from reportlab.lib.styles import getSampleStyleSheet
   from reportlab.lib import colors
   from reportlab.lib.pagesizes import letter
   from reportlab.platypus import Table

   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
               pagesize=letter,
               rightMargin=40,
               leftMargin=40,
               topMargin=60,
               bottomMargin=18,
               )
   ordenes = []
   styles = getSampleStyleSheet()
   header = Paragraph("ORDEN DE TRABAJO|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
   header1 = Paragraph("", styles['Heading3'])
   header2 = Paragraph("Firma Técnico: ________________________", styles['Heading3'])
   header3 = Paragraph("", styles['Heading3'])
   header4 = Paragraph("Firma Cliente: _________________________", styles['Heading3'])
   header5 = Paragraph("", styles['Heading3'])
   ordenes.append(header)
   ordenes.append(header1)
   ordenes.append(header2)
   ordenes.append(header3)
   ordenes.append(header4)
   ordenes.append(header5)
   headings = ('Orden', 'Ingreso', 'Cliente', 'Equipo', 'Costo', 'Entrega', 'Técnico')
   if not pk:
     todasordenes = [(p.id, p.creacion, p.cliente, p.descripcion, p.costo, p.egreso, p.empleado)
               for p in Orden.objects.all().order_by('-pk')]
   else:
     todasordenes = [(p.id, p.creacion, p.cliente, p.descripcion, p.costo, p.egreso, p.empleado)
               for p in Orden.objects.filter(id=pk)]
   t = Table([headings] + todasordenes)
   t.setStyle(TableStyle(
     [
       ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
     ]
   ))
   ordenes.append(t)
   doc.build(ordenes)
   response.write(buff.getvalue())
   buff.close()
   return response

def ordenes_print(self, pk=None):
     import io
     from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
     from reportlab.lib.styles import getSampleStyleSheet
     from reportlab.lib import colors
     from reportlab.lib.pagesizes import letter
     from reportlab.platypus import Table

     response = HttpResponse(content_type='application/pdf')
     buff = io.BytesIO()
     doc = SimpleDocTemplate(buff,
                 pagesize=letter,
                 rightMargin=40,
                 leftMargin=40,
                 topMargin=60,
                 bottomMargin=18,
                 )
     ordenes = []
     styles = getSampleStyleSheet()
     header = Paragraph("LISTADO ORDENES|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
     ordenes.append(header)
     headings = ('Orden', 'Ingreso', 'Cliente', 'Equipo', 'Costo', 'Entrega', 'Técnico')
     if not pk:
       todasordenes = [(p.id, p.creacion, p.cliente, p.descripcion, p.costo, p.egreso, p.empleado)
                 for p in Orden.objects.all().order_by('-pk')]
     t = Table([headings] + todasordenes)
     t.setStyle(TableStyle(
       [
         ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
         ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
         ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
       ]
     ))
     ordenes.append(t)
     doc.build(ordenes)
     response.write(buff.getvalue())
     buff.close()
     return response

def garantia_print(self, pk=None):
   import io
   from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
   from reportlab.lib.styles import getSampleStyleSheet
   from reportlab.lib import colors
   from reportlab.lib.pagesizes import letter
   from reportlab.platypus import Table

   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
               pagesize=letter,
               rightMargin=40,
               leftMargin=40,
               topMargin=60,
               bottomMargin=18,
               )
   garantias = []
   styles = getSampleStyleSheet()
   header = Paragraph("ORDEN GARANTIA|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
   header1 = Paragraph("", styles['Heading3'])
   header2 = Paragraph("Firma Técnico: ___________________", styles['Heading3'])
   header3 = Paragraph("", styles['Heading3'])
   header4 = Paragraph("Firma Cliente: ____________________", styles['Heading3'])
   header5 = Paragraph("", styles['Heading3'])
   garantias.append(header)
   garantias.append(header1)
   garantias.append(header2)
   garantias.append(header3)
   garantias.append(header4)
   garantias.append(header5)
   headings = ('Orden', 'Ingreso', 'Cliente', 'Equipo', 'Costo', 'Entrega', 'Técnico')
   if pk:
     todasgarantias = [(p.id, p.creacion, p.cliente, p.descripcion, p.costo, p.egreso, p.empleado)
               for p in Garantia.objects.filter(id=pk)]
   t = Table([headings] + todasgarantias)
   t.setStyle(TableStyle(
     [
       ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
     ]
   ))
   garantias.append(t)
   doc.build(garantias)
   response.write(buff.getvalue())
   buff.close()
   return response

def garantias_print(self, pk=None):
      import io
      from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
      from reportlab.lib.styles import getSampleStyleSheet
      from reportlab.lib import colors
      from reportlab.lib.pagesizes import letter
      from reportlab.platypus import Table

      response = HttpResponse(content_type='application/pdf')
      buff = io.BytesIO()
      doc = SimpleDocTemplate(buff,
                  pagesize=letter,
                  rightMargin=40,
                  leftMargin=40,
                  topMargin=60,
                  bottomMargin=18,
                  )
      garantias = []
      styles = getSampleStyleSheet()
      header = Paragraph("LISTADO GARANTIAS|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
      garantias.append(header)
      headings = ('Orden', 'Ingreso', 'Cliente', 'Equipo', 'Costo', 'Entrega', 'Técnico')
      if not pk:
        todasgarantias = [(p.id, p.creacion, p.cliente, p.descripcion, p.costo, p.egreso, p.empleado)
                  for p in Garantia.objects.all().order_by('-pk')]

      t = Table([headings] + todasgarantias)
      t.setStyle(TableStyle(
        [
          ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
          ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
          ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
      ))
      garantias.append(t)
      doc.build(garantias)
      response.write(buff.getvalue())
      buff.close()
      return response

def productos_print(self, pk=None):
      import io
      from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
      from reportlab.lib.styles import getSampleStyleSheet
      from reportlab.lib import colors
      from reportlab.lib.pagesizes import letter
      from reportlab.platypus import Table

      response = HttpResponse(content_type='application/pdf')
      buff = io.BytesIO()
      doc = SimpleDocTemplate(buff,
                  pagesize=letter,
                  rightMargin=40,
                  leftMargin=40,
                  topMargin=60,
                  bottomMargin=18,
                  )
      productos = []
      styles = getSampleStyleSheet()
      header = Paragraph("LISTA PRODUCTOS|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
      productos.append(header)
      headings = ('Correlativo', 'Fecha', 'Producto', 'Modelo', 'Marca')
      if not pk:
        todosproductos = [(p.id, p.creacion, p.producto, p.modelo, p.marca)
                  for p in Producto.objects.all().order_by('-pk')]

      t = Table([headings] + todosproductos)
      t.setStyle(TableStyle(
        [
          ('GRID', (0, 0), (5, -1), 1, colors.dodgerblue),
          ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
          ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
      ))
      productos.append(t)
      doc.build(productos)
      response.write(buff.getvalue())
      buff.close()
      return response

def ventas_print(self, pk=None):
      import io
      from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
      from reportlab.lib.styles import getSampleStyleSheet
      from reportlab.lib import colors
      from reportlab.lib.pagesizes import letter
      from reportlab.platypus import Table

      response = HttpResponse(content_type='application/pdf')
      buff = io.BytesIO()
      doc = SimpleDocTemplate(buff,
                  pagesize=letter,
                  rightMargin=40,
                  leftMargin=40,
                  topMargin=60,
                  bottomMargin=18,
                  )
      ventas = []
      styles = getSampleStyleSheet()
      header = Paragraph("LISTA VENTAS|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
      ventas.append(header)
      headings = ('No', 'Fecha', 'Cliente', 'Producto', 'Cantidad', 'Total', 'Empleado')
      if not pk:
        todasventas = [(p.id, p.fechaventa, p.cliente, p.producto, p.cantidad, p.total, p.empleado)
                  for p in Venta.objects.all().order_by('-pk')]

      t = Table([headings] + todasventas)
      t.setStyle(TableStyle(
        [
          ('GRID', (0, 0), (7, -1), 1, colors.dodgerblue),
          ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
          ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
      ))
      ventas.append(t)
      doc.build(ventas)
      response.write(buff.getvalue())
      buff.close()
      return response

def venta_print(self, pk=None):
   import io
   from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
   from reportlab.lib.styles import getSampleStyleSheet
   from reportlab.lib import colors
   from reportlab.lib.pagesizes import letter
   from reportlab.platypus import Table

   response = HttpResponse(content_type='application/pdf')
   buff = io.BytesIO()
   doc = SimpleDocTemplate(buff,
               pagesize=letter,
               rightMargin=40,
               leftMargin=40,
               topMargin=60,
               bottomMargin=18,
               )
   venta = []
   styles = getSampleStyleSheet()
   header = Paragraph("ORDEN DE VENTA|SOPORTE TÉCNICO|COMPUMASTER", styles['Heading1'])
   venta.append(header)
   headings = ('No', 'Fecha', 'Cliente', 'Producto', 'Precio', 'Cantidad', 'Total')
   if pk:
     todasventas = [(p.id, p.fechaventa, p.cliente, p.producto, p.valor, p.cantidad, p.total)
               for p in Venta.objects.filter(id=pk)]
   t = Table([headings] + todasventas)
   t.setStyle(TableStyle(
     [
       ('GRID', (0, 0), (6, -1), 1, colors.dodgerblue),
       ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
       ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
     ]
   ))
   venta.append(t)
   doc.build(venta)
   response.write(buff.getvalue())
   buff.close()
   return response
