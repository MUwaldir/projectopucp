# Generated by Django 4.1 on 2022-09-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion_tareas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tarea",
            name="nombre_tarea",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="tarea",
            name="descripcion",
            field=models.CharField(default="", max_length=500),
        ),
    ]
