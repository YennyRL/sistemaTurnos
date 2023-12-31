# Generated by Django 4.2.5 on 2023-09-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitioTurnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_laborales', models.DateField(max_length=15)),
                ('horario_disponible', models.FloatField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id_especialidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_especialidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id_profesional', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_servicio', models.CharField(max_length=100)),
                ('duracion_servicio', models.FloatField(max_length=15)),
            ],
        ),
    ]
