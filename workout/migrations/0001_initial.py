# Generated by Django 4.1.6 on 2023-04-15 11:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("exercises", "0003_alter_exercises_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Workout",
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
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("duration", models.DurationField()),
                (
                    "exercises",
                    models.ManyToManyField(
                        blank=True, related_name="workout", to="exercises.exercises"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workout",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
