# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delegado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreDelegado', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('fechaIngresoUjc', models.DateField()),
                ('responsabilidad', models.CharField(max_length=30)),
                ('centroTrabajo', models.CharField(max_length=30)),
                ('limitacion', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Delegados',
            },
        ),
        migrations.CreateModel(
            name='Escolaridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoescolaridad', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Escolaridades',
            },
        ),
        migrations.CreateModel(
            name='IntegrantesNucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('fechaNac', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Integrantes del Nucleo',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreProvincia', models.CharField(max_length=30)),
                ('primersecretario', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Embarazadas',
            fields=[
                ('posibleFechaDeParto', models.DateField()),
                ('delegado', models.OneToOneField(primary_key=True, serialize=False, to='ujc.Delegado')),
            ],
            options={
                'verbose_name_plural': 'Embarazadas',
            },
        ),
        migrations.CreateModel(
            name='JefeNucleo',
            fields=[
                ('ocupacion', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('integrante', models.OneToOneField(primary_key=True, serialize=False, to='ujc.IntegrantesNucleo')),
            ],
            options={
                'verbose_name_plural': 'Jefe de Nucleo',
            },
        ),
        migrations.AddField(
            model_name='delegado',
            name='escolaridad',
            field=models.ForeignKey(to='ujc.Escolaridad'),
        ),
        migrations.AddField(
            model_name='delegado',
            name='provincia',
            field=models.ForeignKey(to='ujc.Provincia'),
        ),
    ]
