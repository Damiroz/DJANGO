from django.contrib import admin
from .models import CustomUser, Game


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number', 'date_of_birth')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'developer', 'release_date', 'price')

