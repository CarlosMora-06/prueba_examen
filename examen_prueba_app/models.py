from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=80,unique=True)

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ["nombre"]


class Pedido(models.Model):
    fecha = models.DateField()
    pagado = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ["fecha"]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField(max_length=200)
    precio = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Productos"
        ordering = ["nombre"]



class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Items"


    def __str__(self):
        return self.pedido.nombre
