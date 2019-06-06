from django.contrib import admin
from .models import Book
from .models import Publisher
from .models import Binding

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     lists_display =['id','Title','ISBN_10','Author','Binding','Year','Publisher']

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
     lists_display =['id','name']

@admin.register(Binding)
class BindingAdmin(admin.ModelAdmin):
     lists_display =['id','name']



