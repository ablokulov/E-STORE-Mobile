from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at")
    search_fields = ("name", "slug")
    list_filter = ("created_at",)

    readonly_fields = ("slug", "created_at")

    
    