from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Opinion(models.Model):
    nombre = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}: {self.mensaje[:30]}..."

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    es_cliente = models.BooleanField(default=True)
    es_vendedor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} ({'Cliente' if self.es_cliente else 'Vendedor'})"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="productos/")
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.nombre



class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default="simulado")

    def __str__(self):
        return f"{self.usuario.username} - {self.metodo_pago} - {self.total} ARS"
