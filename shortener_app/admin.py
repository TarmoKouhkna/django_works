from django.contrib import admin
from .models import ShortenedURL, AliasedUrl

@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at')

@admin.register(AliasedUrl)
class AliasedUrlAdmin(admin.ModelAdmin):
    list_display = ('url', 'alias')
