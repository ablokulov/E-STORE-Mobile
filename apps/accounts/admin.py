from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Address


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    
    list_display = ("id", "username", "email", "role", "is_staff", "is_active","date_joined","last_login")
    list_filter = ("role","is_staff", "is_active","date_joined")
    search_fields = ("username", "email")

    fieldsets = UserAdmin.fieldsets + (
        ("Role info", {"fields": ("role",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",          
                "password1",
                "password2",
                "role",
            ),
        }),
    )

    search_fields = ("username", "email")
    ordering = ("username",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","first_name","last_name","phone")
    search_fields = ("user__email",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "street", "is_default")
    list_filter = ("city", "is_default")
    search_fields = ("user__email", "city")
