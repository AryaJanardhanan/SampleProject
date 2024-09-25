from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Item)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','pub_year')
    search_fields = ('title','author')
    list_filter = ('pub_year', 'author')





