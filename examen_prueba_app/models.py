from django.db import models


from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name_plural = "Autores"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20)
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    autor = models.ForeignKey(
        Autor,
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name_plural = "Libros"
        ordering = ['-pk']

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class LibroCategoria(models.Model):
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Libros por categorías"
        ordering = ['-pk']

    def __str__(self):
        return f"{self.libro.titulo} - {self.categoria.nombre}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=20)
    total = models.PositiveIntegerField()
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name_plural = "Pedidos"
        ordering = ['-pk']

    def __str__(self):
        return str(self.fecha)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro,
        on_delete=models.PROTECT
    )
    cantidad = models.PositiveIntegerField()
    preciounitario = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Detalles de pedidos"
        ordering = ['-pk']

    def __str__(self):
        return f"Detalle del pedido {self.pedido_id}"
