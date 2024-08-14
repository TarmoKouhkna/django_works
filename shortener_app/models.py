from django.db import models

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_short_url(self):
        return f"http://short.url/{self.short_code}"

    def __str__(self):
        return self.short_code


class AliasedUrl(models.Model):
    url = models.URLField()
    alias = models.CharField(max_length=255, unique=True)  # Ensure the alias is unique

    def __str__(self):
        return self.alias
