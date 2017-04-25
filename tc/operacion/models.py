from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Comisionista(models.Model):
    comisionista_nombre = models.CharField(max_length=250)
    comisionista_cuenta = models.IntegerField()
    comisionista_rfc = models.CharField(max_length=250)
    comisionista_telefono = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str___(self):
        return self.comisionista_nombre


class Cliente(models.Model):
    STATUS_CHOICES = (
        ('activo', 'Activo'),
        ('baja', 'Baja'),
    )
    # cliente_id = models.AutoField() se genera en automatico un id por django
    cliente_nombre = models.CharField(max_length=250)
    cliente_calle = models.CharField(max_length=250)
    cliente_numext = models.IntegerField()
    cliente_numint = models.CharField(max_length=250)
    cliente_colonia = models.CharField(max_length=250)
    cliente_del_mun = models.CharField(max_length=250)
    cliente_cp = models.IntegerField()
    cliente_telefono = models.BigIntegerField()
    cliente_rfc = models.CharField(max_length=14)
    cliente_alta = models.DateTimeField(auto_now_add=True)
    cliente_umodificacion = models.DateTimeField(auto_now=True)
    cliente_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='activo')
    cliente_alta = models.ForeignKey(User, related_name='altas_usuario')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.cliente_nombre


class Empresa(models.Model):
    empresa_mombre = models.CharField(max_length=250)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.Empresa


class Costo(models.Model):
    costo_cliente = models.ForeignKey(Cliente, related_name="costo_cliente")
    costo_efectivo = models.IntegerField()
    costo_total = models.IntegerField()
    costo_comisionista = models.IntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.cliente_nombre


class Movimiento(models.Model):
    movimiento_cliente = models.ForeignKey(
        Cliente, related_name='movimiento_cliente')
    movimiento_fecha = models.DateField(auto_now_add=True)
    movimiento_umodificacion = models.DateTimeField(auto_now=True)
    movimiento_factura = models.CharField(max_length=20)
    movimiento_banco = models.CharField(max_length=25)
    movimiento_regreso_total = models.IntegerField()
    movimiento_referencia = models.IntegerField()
    movimiento_empresa = models.ForeignKey(
        Empresa, related_name='movimiento_empresa')

    class Meta:
        ordering = ['id']


class Regreso(models.Model):
    STATUS_CHOICES = (
        ('efectivo', 'Efectivo'),
        ('cheque', 'Cheque'),
        ('transferencia', 'Transferencia')
    )
    regreso_movimiento = models.ForeignKey(
        Movimiento, related_name='regresos_movimiento')
    regreso_monto = models.IntegerField()
    regreso_tipo = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='cheque')

    class Meta:
        ordering = ['id']


class MovimientoComisionista(models.Model):
    MovimientoComisionista_movimiento = models.ForeignKey(
        Movimiento, related_name='movientocomisionista')
    MovimientoComisionista_comisionista = models.ForeignKey(
        Comisionista, related_name='comisionistamovimiento')

    class Meta:
        ordering = ['id']
