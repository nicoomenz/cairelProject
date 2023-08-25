from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'

class Product(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=15)
    slug = AutoSlugField(populate_from='name')
    patent = models.CharField(max_length=15)
    description = models.TextField(null= True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    active = models.BooleanField(default=True)
