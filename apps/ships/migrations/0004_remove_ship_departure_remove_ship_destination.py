# Generated by Django 4.1.9 on 2023-05-27 17:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ships", "0003_alter_ship_departure_alter_ship_departure_symbol_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ship",
            name="departure",
        ),
        migrations.RemoveField(
            model_name="ship",
            name="destination",
        ),
    ]