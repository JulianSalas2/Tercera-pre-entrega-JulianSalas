# Generated by Django 5.1.3 on 2024-11-25 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_entregable_estudiante_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('id_estudiante', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Envio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fecha_de_entrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('anio_fundacion', models.DateField()),
                ('ubicacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameModel(
            old_name='Profesor',
            new_name='Docente',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
    ]
