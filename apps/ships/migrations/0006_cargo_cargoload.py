# Generated by Django 4.1.9 on 2023-06-06 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("markets", "0012_alter_tradegood_tradegood_name"),
        ("ships", "0005_ship_flightmode_ship_location_current_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cargo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cargo_name", models.CharField(max_length=60)),
                ("cargo_capacity", models.IntegerField(blank=True, null=True)),
                ("units_held", models.IntegerField(blank=True, null=True)),
                ("cargo_fill", models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
                ("full_cargo", models.BooleanField(default=False)),
                ("ship", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="ships.ship")),
            ],
        ),
        migrations.CreateModel(
            name="CargoLoad",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("symbol", models.CharField(max_length=60)),
                ("units", models.IntegerField(blank=True, null=True)),
                (
                    "cargo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="cargoload", to="ships.cargo"
                    ),
                ),
                (
                    "good",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="cargogoods", to="markets.good"
                    ),
                ),
            ],
        ),
    ]