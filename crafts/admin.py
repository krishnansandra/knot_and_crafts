from django.contrib import admin
from .models import Product, ContactMessage,Category
from django.utils.html import format_html


class BaseStyledAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }

@admin.register(ContactMessage)
class ContactMessageAdmin(BaseStyledAdmin):
    list_display = ('name','email', 'message','created_at')


@admin.register(Category)
class CategoryAdmin(BaseStyledAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(BaseStyledAdmin):
    list_display = ('title', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}
    