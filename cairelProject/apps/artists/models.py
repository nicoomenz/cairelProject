from django.db import models

# Create your models here.

class Rol(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Roles'

class Person(models.Model):
    age = models.DateField()
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    biography = models.TextField(null=True, blank=True)
