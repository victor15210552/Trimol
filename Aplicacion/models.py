from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db.models import permalink

class Usuario(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	email = models.EmailField(default='fdsafs@fdasf.com')
	image = models.ImageField( blank=True, null=True)
	Direccion=models.CharField(max_length=30)
	Alergias = models.CharField(max_length=30,default='None')
	TipodeSangre=models.CharField(max_length=10,default='None')
	def __str__(self):
		return "Name: %s"%(self.Direccion)


class Especialidad (models.Model):	
	Especialidad=models.CharField(max_length=200)
	Descripcion=models.TextField()	
	def __str__(self):
		return "Especialidad: %s"%(self.Especialidad)





class Sector(models.Model):	
	Sector=models.CharField(max_length=10)
	Descripcion=models.TextField()
	def __str__(self):
		return "Sector: %s"%(self.Sector)

class Estado(models.Model):
	Ciudad=models.CharField(max_length=45,default='Tijuana')
	Estado=models.CharField(max_length=45,default='Baja California')
	def __str__(self):
		return "Ciudad: %s, Estado: %s"%(self.Ciudad, self.Estado)

#Metodo para listado de autorizados 




class publicacionmanager(models.Manager):
	def get_queryset(self):
		return super(publicacionmanager,self).get_queryset().filter(autorizado=True).order_by('creado','calificacion')


class Hospital(models.Model):
	Nombre=models.CharField(max_length=40,default='Hospital')
	Sector=models.ForeignKey(Sector, on_delete=models.CASCADE)
	Direccion=models.CharField(max_length=100)
	Ciudad=models.ForeignKey(Estado, on_delete=models.CASCADE)
	Telefono=models.CharField(max_length=25)
	Especialidad=models.TextField(default='Ninguna')
	Pagina_Oficial=models.URLField(max_length=200,default='None')
	Horario=models.CharField(max_length=20,default='24 Horas')
	Correo=models.EmailField(max_length=30,default='None')
	slug=models.SlugField(max_length=30,unique=True)
#Prueba Like
	calificacion=models.IntegerField(default=0)
	Imagen=models.ImageField(blank=True, null=True)
	Latitud=models.FloatField()
	Longitud=models.FloatField()
#Prueba para view dinamic	
	autorizado=models.BooleanField(default=False)
	creado=models.DateField(auto_now_add=True)
	objects=models.Manager()
	autorizados_objects=publicacionmanager()
	#end
	def __str__(self):
		return "Nombre: %s"%(self.Nombre)

	def like(self):
		self.calificacion=self.calificacion+1
		self.save()
		return 'Calificacion actual: %s' % self.calificacion

	@permalink
	def get_absolute_url(self):
		return ('pub-detail', None, { 'pk': self.pk })
		
class Ubicacion(models.Model):
	Latitud=models.FloatField()
	Longitud=models.FloatField()
	Hospital=models.ForeignKey("Hospital", on_delete=models.CASCADE)
	def __str__(self):
		return "Latitud: %s, Longitud: %s"%(self.Latitud, self.Longitud)
