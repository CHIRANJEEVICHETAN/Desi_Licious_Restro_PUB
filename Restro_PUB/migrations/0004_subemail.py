# Generated by Django 4.2.6 on 2023-11-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Restro_PUB", "0003_contactus_alter_booktable_tdate_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubEmail",
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
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]