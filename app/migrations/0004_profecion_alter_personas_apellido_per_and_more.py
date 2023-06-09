# Generated by Django 4.2 on 2023-05-06 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_persona_personas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profecion',
            fields=[
                ('id_profecion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id profecion')),
                ('nombreProfecion', models.CharField(max_length=50, verbose_name='Profecion')),
            ],
        ),
        migrations.AlterField(
            model_name='personas',
            name='apellido_per',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='clave_per',
            field=models.CharField(max_length=20, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='codPostal_per',
            field=models.IntegerField(verbose_name='Codigo postal'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='correo_per',
            field=models.CharField(max_length=30, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='id_per',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombre_per',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='personas',
            name='Profecion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.profecion'),
        ),
    ]
