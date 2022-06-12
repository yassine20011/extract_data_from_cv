from django.contrib import admin
from .models import upload_file
# Register your models here.

@admin.register(upload_file)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
