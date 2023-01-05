from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django import forms
import random



class Info(models.Model):
    number = models.AutoField(primary_key=True)
    animal = models.CharField('Breed', max_length=120, default='', blank=True, null=True)
    date = models.DateField(auto_now_add=False, auto_now=True)
    name = models.CharField('Name', max_length=120, default='', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    image = models.ImageField('Image(Optional)', upload_to='Reference/', blank=True)
    comments = models.TextField('Description', max_length=3000, default='', blank=True, null=True)

    def __str__(self):
        return self.animal

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(str(f"{random.randint(100000000000,999999999998)}"), writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f"{self.name}{self.animal}.png", File(buffer), save=False)
        return super().save(*args, **kwargs)

