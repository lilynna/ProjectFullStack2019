from django.db import models

# Create your models here.
class Binding(models.Model):
    name = models.CharField(max_length=255)
     def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)
     def __str__(self):
        return self.name

class book(models.Model):
    title = models.CharField(max_length=255)
    ISBN_10 = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Binding = models.ForeignKey(Binding, 
                                on_delete=models.SET_NULL, 
                                null=True)
    Year = models.PositiveSmallInteger()
    Publisher = models.ForeignKey(Publisher, 
                                on_delete=models.SET_NULL, 
                                null=True)
