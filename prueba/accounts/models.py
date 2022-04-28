from django.db import models

class Administrador(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    correo = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    admin = models.ForeignKey(Administrador, on_delete=models.CASCADE, null=True)
    nit = models.CharField(max_length=10, null=True)
    nombreEmpresa = models.CharField(max_length=100, null=True)
    nombreComercialEmpresa = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=10, null=True)
    correo = models.EmailField()
    sitioWeb = models.URLField(max_length=50)
    ciudad = models.CharField(max_length=20, null=True)
    pais = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nombreEmpresa


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    apellido = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=10, null=True)
    correo = models.EmailField()
    ciudad = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre + self.apellido

class Sede(models.Model):
    nombreSede = models.CharField(max_length=200, null=True)
    direccion = models.CharField(max_length=10, null=True)
    correo = models.EmailField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    geolocalizacion = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=10, null=True)
    horarios = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nombreSede


class Horario(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, null=True)
    horaInicio = models.TimeField(null=True)
    horaFin = models.TimeField(null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
