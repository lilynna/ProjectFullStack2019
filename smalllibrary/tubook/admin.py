from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =[i.title for i in Book._meta.fields]
