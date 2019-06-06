from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
     list_display =['id','Title','ISBN_10','Author','Binding','Year','Publisher']
