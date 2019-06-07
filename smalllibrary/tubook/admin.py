from django.contrib import admin
from .models import Book,Publisher,Binding,Transaction

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display =[f.name for f in Book._meta.fields]

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
     list_display =['id','name']

@admin.register(Binding)
class BindingAdmin(admin.ModelAdmin):
     list_display =['id','name']

@admin.register(Transaction)
class BindingAdmin(admin.ModelAdmin):
     list_display =[f.name for f in Transaction._meta.fields]


