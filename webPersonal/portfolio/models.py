from django.db import models

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=200, verbose_name="Titulo")
    decription= models.TextField(verbose_name="Descripcion")
    image= models.ImageField(verbose_name="imagen", upload_to="projects")
    link=models.URLField(verbose_name="Direccion web", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="ultima actualizacion")

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
        ordering=["-created"]
    
    def __str__(self):
        return self.title
        

