from django.contrib import admin
from ui.models import Login

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
