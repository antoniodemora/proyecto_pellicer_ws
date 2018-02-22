from django.db import models


class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey('Municipio', models.CASCADE)


    def __str__(self):
        return self.nombre + ", " + str(self.municipio)


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.ForeignKey('Estado', models.CASCADE)

    def __str__(self):
        return self.nombre + ", " + str(self.estado)


class Estado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre