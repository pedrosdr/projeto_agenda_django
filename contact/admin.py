from django.contrib import admin
from contact.models import Contact
from contact.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    ordering = ('name',)
    list_per_page = 10
    list_max_show_all = 200

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'category')
    ordering = ('-id',)
    list_per_page = 10
    list_max_show_all = 200
