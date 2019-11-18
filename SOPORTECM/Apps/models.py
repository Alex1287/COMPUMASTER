# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=45, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    fechaegreso = models.DateField(db_column='FechaEgreso', blank=True, null=True)  # Field name made lowercase.
    entregado = models.IntegerField(db_column='Entregado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Costos(models.Model):
    idcostos = models.AutoField(db_column='idCostos', primary_key=True)  # Field name made lowercase.
    costo = models.FloatField(db_column='Costo', blank=True, null=True)  # Field name made lowercase.
    cancelado = models.IntegerField(db_column='Cancelado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'costos'


class DetalleProducto(models.Model):
    iddetalle_producto = models.AutoField(db_column='idDetalle_Producto', primary_key=True)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalle_producto'


class Empleados(models.Model):
    idempleados = models.AutoField(db_column='idEmpleados', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='Nombres', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    puesto = models.CharField(db_column='Puesto', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleados'


class Equipo(models.Model):
    idequipo = models.AutoField(db_column='idEquipo', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    problema = models.CharField(db_column='Problema', max_length=45, blank=True, null=True)  # Field name made lowercase.
    solucion = models.CharField(db_column='Solucion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.
    costos_idcostos = models.ForeignKey(Costos, models.DO_NOTHING, db_column='Costos_idCostos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipo'


class Garantias(models.Model):
    idgarantias = models.AutoField(db_column='idGarantias', primary_key=True)  # Field name made lowercase.
    empleados_idempleados = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Empleados_idEmpleados')  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'garantias'


class Ordenes(models.Model):
    idordenes = models.AutoField(db_column='idOrdenes', primary_key=True)  # Field name made lowercase.
    empleados_idempleados = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Empleados_idEmpleados')  # Field name made lowercase.
    cliente_idcliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_idCliente')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenes'


class Producto(models.Model):
    idproducto = models.AutoField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    producto = models.CharField(db_column='Producto', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    fechapedido = models.DateField(db_column='FechaPedido', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    detalle_producto_iddetalle_producto = models.ForeignKey(DetalleProducto, models.DO_NOTHING, db_column='Detalle_Producto_idDetalle_Producto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Roles(models.Model):
    idroles = models.AutoField(db_column='idRoles', primary_key=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Usuarios(models.Model):
    idusuarios = models.AutoField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=45, blank=True, null=True)  # Field name made lowercase.
    empleados_idempleados = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Empleados_idEmpleados')  # Field name made lowercase.
    roles_idroles = models.ForeignKey(Roles, models.DO_NOTHING, db_column='Roles_idRoles')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'
