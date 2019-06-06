from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
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
    def __str__(self):
        return self.name
                                    
class Borrow(models.Model):
    Borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)
     def __str__(self):
        return self.name

class Binding(models.Model):
    name = models.CharField(max_length=255)
     def __str__(self):
        return self.name

class Transaction(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    Actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Action = models.CharField(max_length=255)
    Created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.name