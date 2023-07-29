from django.db import models


#Create your models here.

class Sexo(models.Model):
    tipo = models.CharField(max_length = 10)
    def __str__(self):
        return self.tipo

class Limitacion(models.Model):
    tipo = models.CharField(max_length = 2)
    def __str__(self):
        return self.tipo


class Provincia(models.Model):
    nombreProvincia = models.CharField(max_length=30)
    primersecretario = models.CharField(max_length=30)


    def __str__(self):
        return self.nombreProvincia

    class Meta:
        verbose_name_plural = 'Provincias'

class Escolaridad(models.Model):
    tipoescolaridad = models.CharField(max_length = 20)

    def __str__(self):
        return self.tipoescolaridad

    class Meta:
        verbose_name_plural = 'Escolaridades'

class Casa(models.Model):
    direccion = models.CharField(max_length = 30)
    cantDelegados = models.IntegerField()
    #direccion = models.CharField(max_length = 30)

    def __str__(self):
        return self.direccion

    class Meta:
        verbose_name_plural = 'Casas'

class Delegado(models.Model):
    nombreDelegado = models.CharField(max_length=30)
    edad = models.IntegerField()
    #sexo = models.CharField(max_length=10)
    sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    fechaIngresoUjc = models.DateField()
    responsabilidad = models.CharField(max_length=30)
    centroTrabajo = models.CharField(max_length=30)
    #limitacion = models.CharField(max_length=3)
    provincia = models.ForeignKey(Provincia,on_delete=models.CASCADE)
    escolaridad = models.ForeignKey(Escolaridad,on_delete=models.CASCADE)
    casa = models.ForeignKey(Casa,on_delete=models.CASCADE)
    limitacion = models.ForeignKey(Limitacion,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreDelegado

    def getLimitacion(self):
        return self.limitacion

    def getEdad(self):
        return self.edad

    # def getEscolaridad(self):
    #     return self.escolaridad

    class Meta:
        verbose_name_plural = 'Delegados'

class IntegrantesNucleo(models.Model):
    nombre = models.CharField(max_length = 30)
    fechaNac = models.DateField()
    sexo = models.ForeignKey(Sexo,on_delete=models.CASCADE)
    #casa = models.ForeignKey(Casa,on_delete=models.CASCADE, default=1)
    casa = models.ForeignKey(Casa,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Integrantes del Nucleo'

class JefeNucleo(models.Model):
    ocupacion = models.CharField(max_length = 30)
    
    edad = models.IntegerField()
    integrante = models.OneToOneField(IntegrantesNucleo, on_delete=models.CASCADE)

    def __str__(self):
        return self.integrante

    class Meta:
        verbose_name_plural = 'Jefe de Nucleo'

class Embarazadas(Delegado):

    posibleFechaDeParto = models.DateField()

    def __str__(self):
        return self.posibleFechaDeParto

    class Meta:
        verbose_name_plural = 'Embarazadas'

# class User(Delegado):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.EmailField()
#     firstname = models.CharField(max_length=20)
#     lastname = models.CharField(max_length=20)
        #, 'password', 'email', 'firstname', 'lastname'
    # def __str__(self):
    #     return self.posibleFechaDeParto
    #
    # class Meta:
    #     verbose_name_plural = 'Embarazadas'

