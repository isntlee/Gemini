# Generated by Django 4.1.9 on 2023-05-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("extractions", "0002_extraction_cargo_fill"),
    ]

    operations = [
        migrations.AddField(
            model_name="extraction",
            name="extraction_name",
            field=models.CharField(default="pre-set string", max_length=200),
            preserve_default=False,
        ),
    ]