# Generated by Django 4.1.9 on 2023-05-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("markets", "0008_markettrade_tradegood_remove_good_markets_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="good",
            name="description",
            field=models.CharField(max_length=500),
        ),
    ]