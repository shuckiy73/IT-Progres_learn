# Generated by Django 4.2.2 on 2023-06-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_1", "0002_mebel_delete_car"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mebel",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
