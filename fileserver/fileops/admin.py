from django.contrib import admin
from .models import Files

class FileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Files, FileAdmin)
