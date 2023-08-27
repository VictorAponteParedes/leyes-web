from django.db import models

# Create your models here.

class Caso(models.Model):
    MATERIA_CHOICES = (
        ('laboral', 'Laboral'),
        ('civil y comercial', 'Civil y Comercial'),
        ('administrativo', 'Administrativo'),
        ('penal', 'Penal'),
        ('niñez y adolecencia', 'Niñez y Adolecencia'),
    )
    nombre = models.CharField(max_length=40, help_text="Ingrese el nombre del caso")
    nro_expediente = models.IntegerField(default=0, help_text="Ingrese en numero de expediente")
    fecha = models.DateField()
    materia = models.CharField(max_length=20, choices=MATERIA_CHOICES, default="laboral")
    juzgado = models.CharField(max_length=100, help_text="Ingrese el nombre del Juzgado", default="")
    foto_perfil = models.ImageField(upload_to ='media/', null=True, blank=True)
 

    def __str__(self):
        return self.nombre
    


class Cliente(models.Model):
     nombre = models.CharField(max_length=50, help_text="Ingrese el numero del cliente")
     edad = models.IntegerField("Edad", blank=False, help_text="Ingrese su edad", default=18)
     telefono = models.IntegerField("Celular", help_text="Ingrese su numero de telefono", default=None)
     caso_relacionado = models.ForeignKey(Caso, on_delete=models.CASCADE)
     is_activo = models.BooleanField(default=False)
     foto_perfil = models.ImageField(upload_to ='media/', null=True, blank=True)

     def __str__(self):
        return self.nombre


class Abogado(models.Model):
    ESPECIALIDAD = (
        ('laboral', 'Laboral'),
        ('civil y comercial', 'Civil y Comercial'),
        ('administrativo', 'Administrativo'),
        ('penal', 'Penal'),
        ('niñez y adolecencia', 'Niñez y Adolecencia'),
    )
    nombre = models.CharField("Nombre", max_length=50, help_text="Ingrese su nombre")
    edad = models.IntegerField("Edad", null=True, blank=True, help_text="Ingrese su edad", default=20)
    telefono = models.IntegerField("Celular", help_text="Ingrese su numero de telefono", default=None)
    cliente_relacionado = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to ='media/', null=True, blank=True)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDAD, default="laboral")
    descripcion = models.TextField(help_text="Experiencia, estudio, idioma, certificaciones, etc.", null=True, blank=True, default="descripcion")

    def __str__(self):
        return self.nombre
    

class Rolpersona(models.Model):
    ROL = (
            ('vacio', '-------'),
            ('cliente', 'Cliente'),
            ('abogado', 'Abogado'),
        )
    
    rol = models.CharField(max_length=10, help_text="Selecciona tu rol", choices=ROL, default='vacio')

    def __str__(self):
        return self.rol