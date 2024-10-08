# Generated by Django 5.1 on 2024-08-12 08:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shortener_app", "0003_alter_aliasedurl_alias"),
    ]

    operations = [
        migrations.CreateModel(
            name="URLAlias",
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
                ("url", models.URLField()),
                ("alias", models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
