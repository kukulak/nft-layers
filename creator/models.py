from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class UpImage(models.Model):
    class Rarity_level(models.IntegerChoices):
        NORMAL = 50
        MEDIUM = 40
        RARE = 5
        SUPERRARE = 4
        UNIQUE = 1

    image_name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    up_date = models.DateTimeField(auto_now_add=True, blank=True)
    upload_img = models.ImageField(upload_to='imagesLayers/')
    rarity = models.IntegerField(choices=Rarity_level.choices)
    def __str__(self):
        return self.image_name


class groupImage(models.Model):
    groupImage_name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    up_date = models.DateTimeField(auto_now_add=True, blank=True)
    layer_images = models.ManyToManyField(UpImage, blank=True)
    def __str__(self):
        return self.groupImage_name      


class Efectos(models.Model):
    efecto_name = models.CharField(max_length=200)
    efecto_description = models.TextField(blank=True)
    efecto_codigo = models.TextField(blank=True)
    efecto_value1 = models.IntegerField(blank=True)
    efecto_value2 = models.IntegerField(blank=True)
    efecto_value3 = models.IntegerField(blank=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.efecto_name


class Compound(models.Model):
    compound_name = models.CharField(max_length=200)
    # layer_images = models.ForeignKey(UpImages, on_delete=models.CASCADE)
    up_images = models.ManyToManyField(UpImage, blank=True)
    group_images = models.ManyToManyField(groupImage, blank=True)
    active = models.BooleanField(default=True)
    up_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_img = models.ImageField(upload_to='imagesCompound/', blank=True)

    def __str__(self):
        return self.compound_name

class Layer(models.Model):
    layer_name = models.CharField(max_length=200)
    compound = models.ManyToManyField(Compound, blank=True)
    active = models.BooleanField(default=True)
    up_date = models.DateTimeField(auto_now_add=True, blank=True)
    zindex = models.IntegerField(default=1)
    def __str__(self):
        return self.layer_name

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    file_size_w = models.IntegerField(default=2000, blank=True)
    file_size_h = models.IntegerField(default=2000, blank=True)
    project_layers = models.ManyToManyField(Layer, blank=True)
    active = models.BooleanField(default=True)
    up_date = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.project_name
