# Generated by Django 4.1.5 on 2023-01-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formula_1', '0004_alter_circuitos_capacidad_alter_circuitos_longitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posicion_pilotos_2022',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('conductor', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
                ('auto', models.CharField(max_length=30)),
                ('puntos', models.CharField(max_length=10)),
            ],
        ),
    ]