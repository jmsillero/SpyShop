from django.db import models
from django.utils import timezone

# Create your models here.


# Modelo categoria....
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category', null=True)


    def __str__(self):
        return self.name


class Promotion(models.Model):
    image = models.ForeignKey('Image', blank=True, null=True)
    product = models.ForeignKey('Product', blank=True, null=True)
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name




# Modelo tags...
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



# Modelo producto...
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey('Category')
    tags = models.ManyToManyField('Tag')
    serial = models.CharField(max_length=255, default='')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.name




#Modelo imagen....
class Image(models.Model):
    name = models.CharField(max_length=255)
    src = models.ImageField()
    product = models.ForeignKey('Product', blank=True, null=True)

    def __str__(self):
        return self.name