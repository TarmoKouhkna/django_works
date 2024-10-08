# Generated by Django 5.1 on 2024-08-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shortener_app", "0004_urlalias"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShortenedURL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_url", models.URLField()),
                ("short_code", models.CharField(max_length=10, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="URLAlias",
        ),
        migrations.AlterField(
            model_name="aliasedurl",
            name="alias",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
