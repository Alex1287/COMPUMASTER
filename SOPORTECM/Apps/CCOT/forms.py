from django import forms
from .models import Producto, Empleado, Usuario, Cliente, Orden, Garantia, Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuarioEmailForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets ={
        'contrasena': forms.TextInput(attrs={'class':'form-control', 'type':'password'}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class OrdenesForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'

class GarantiasForm(forms.ModelForm):
    class Meta:
        model = Garantia
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
