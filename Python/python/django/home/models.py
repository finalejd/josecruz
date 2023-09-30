from django.db import models

# 1. Un modelo para una persona

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

# 2. Un modelo para un producto

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# 3. Un modelo para una orden

class Orden(models.Model):
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return self.productos

# 4. Un modelo para una mascota

class Mascota(models.Model):
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

# 5. Un modelo para un libro

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=255)
    paginas = models.IntegerField()
    
    def __str__(self):
        return self.titulo

# 6. Un modelo para una película

class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    actores = models.ManyToManyField('Persona')
    fecha_estreno = models.DateField()

    def __str__(self):
        return self.titulo

# 7. Un modelo para un artículo de blog

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

# 8. Un modelo para un comentario

class Comentario(models.Model):
    autor = models.ForeignKey('Persona', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField()

    def __str__(self):
        return self.autor

# 9. Un modelo para una calificación
class Calificacion(models.Model):
    valor = models.IntegerField()
    comentario = models.TextField()
    autor = models.ForeignKey(Persona, on_delete=models.CASCADE)
    objeto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor

# 10. Un modelo para una imagen

class Imagen(models.Model):
    nombre = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.nombre

