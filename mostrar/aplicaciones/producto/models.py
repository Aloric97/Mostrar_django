from django.db import models

class producto(models.Model):
    nombre = models.CharField(max_length=30)
    tipo= models.CharField(max_length=50)
    cantidad= models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return 'nombre: '+ self.nombre + " tipo: " + self.tipo + " cantidad: " + str(self.cantidad)

    class Meta:

        db_table = 'producto'


