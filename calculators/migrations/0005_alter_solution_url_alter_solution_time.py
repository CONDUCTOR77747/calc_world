# Generated by Django 4.1 on 2024-05-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calculators", "0004_remove_solution_calculator"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solution",
            name="URL",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="solution",
            name="time",
            field=models.DateTimeField(),
        ),
    ]