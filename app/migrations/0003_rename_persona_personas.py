# Generated by Django 4.2 on 2023-05-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comuna_region_delete_empresa_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Persona',
            new_name='Personas',
        ),
    ]
