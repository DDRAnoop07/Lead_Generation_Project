# Generated by Django 4.1.3 on 2022-12-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("LeadGenerationAPP", "0002_alter_employee_dob_alter_employee_photograph"),
    ]

    operations = [
        migrations.CreateModel(
            name="States",
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
                ("stateid", models.IntegerField()),
                ("statename", models.CharField(default="", max_length=45)),
            ],
        ),
    ]
