# Generated by Django 4.1.3 on 2023-01-10 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LeadGenerationAPP", "0009_remove_customer_gender"),
    ]

    operations = [
        migrations.CreateModel(
            name="Administrator",
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
                ("mobileno", models.CharField(default="", max_length=45)),
                ("adminname", models.CharField(default="", max_length=45)),
                ("password", models.CharField(default="", max_length=45)),
            ],
        ),
    ]
