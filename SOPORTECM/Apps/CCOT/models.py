from django.db import models


class Producto(models.Model):
    producto = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s' % (self.producto, self.modelo, self.marca)


class Empleado(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    puesto = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)


class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    rol =  (
        ('Administrador', 'Administrador'),
        ('Tecnico', 'Tecnico'),
        )
    rol = models.CharField(
    max_length = 15,
    choices = rol,
    default = 'Administrador',
    )
    activo = models.BooleanField(default = True)
    creacion = models.DateField(auto_now_add=True)
    empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)

    def __str__(self):
        return (self.usuario)

class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50)
    creacion = models.DateField(auto_now_add=True)


    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

class Orden(models.Model):

    descripcion = models.CharField(max_length=100)
    problema = models.CharField(max_length=100)
    solucion = models.CharField(max_length=100)
    observacion = models.CharField(max_length=200)
    egreso = models.DateField()
    costo = models.FloatField()
    cancelado = models.BooleanField(default = False)
    entregado = models.BooleanField(default = False)
    creacion = models.DateField(auto_now_add=True)
    empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)


    def __str__(self):
        return '%s %s' % (self.descripcion, self.problema)


class Garantia(models.Model):
        descripcion = models.CharField(max_length=100)
        problema = models.CharField(max_length=100)
        solucion = models.CharField(max_length=100)
        observacion = models.CharField(max_length=200)
        egreso = models.DateField()
        costo = models.FloatField()
        cancelado = models.BooleanField(default = False)
        entregado = models.BooleanField(default = False)
        creacion = models.DateField(auto_now_add=True)
        empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
        cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)


        def __str__(self):
            return '%s %s' % (self.descripcion, self.problema)


class Venta(models.Model):
        cantidad = models.FloatField()
        fechaventa = models.DateField(auto_now_add=True)
        valor = models.FloatField()
        total = models.FloatField()
        cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
        empleado = models.ForeignKey(Empleado, on_delete = models.CASCADE)
        producto = models.ForeignKey(Producto, on_delete = models.CASCADE)

        def __str__(self):
            return '%s %s' % (self.cliente, self.producto)
