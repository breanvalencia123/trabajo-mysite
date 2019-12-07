from django.db import models

# Create your models here.
class Bicicleta(models.Model):
	id 		=models.IntegerField(primary_key=True)
	title 	=models.CharField(max_length=200, verbose_name="Nombre")
	botonurl 	=models.CharField(max_length=200,null=False,verbose_name="Cargar imagen")
	imagenurl 	=models.CharField(max_length=200,null=False,verbose_name="Direccion imagen")
	creada =models.DateTimeField(auto_now_add=True)
	updateada =models.DateTimeField(auto_now=True)
