# Generated by Django 4.1.5 on 2023-02-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Taxi",
            fields=[
                ("capacity", models.IntegerField()),
                ("passengers", models.IntegerField()),
                ("fare", models.FloatField()),
                (
                    "taxi_number",
                    models.IntegerField(default=111, primary_key=True, serialize=False),
                ),
                ("taxi_type", models.TextField()),
                ("notes", models.TextField()),
                ("occupied", models.BooleanField()),
            ],
        ),
    ]