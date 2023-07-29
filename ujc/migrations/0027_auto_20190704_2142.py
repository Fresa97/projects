# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0026_auto_20190704_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=30)),
                ('cantDelegados', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Casas',
            },
        ),
        migrations.CreateModel(
            name='Delegado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreDelegado', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('fechaIngresoUjc', models.DateField()),
                ('responsabilidad', models.CharField(max_length=30)),
                ('centroTrabajo', models.CharField(max_length=30)),
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
                ('casa', models.ForeignKey(to='ujc.Casa')),
            ],
            options={
                'verbose_name_plural': 'Integrantes del Nucleo',
            },
        ),
        migrations.CreateModel(
            name='JefeNucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocupacion', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('integrante', models.OneToOneField(to='ujc.IntegrantesNucleo')),
            ],
            options={
                'verbose_name_plural': 'Jefe de Nucleo',
            },
        ),
        migrations.CreateModel(
            name='Limitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=2)),
            ],
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
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Embarazadas',
            fields=[
                ('delegado_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ujc.Delegado')),
                ('posibleFechaDeParto', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Embarazadas',
            },
            bases=('ujc.delegado',),
        ),
        migrations.AddField(
            model_name='integrantesnucleo',
            name='sexo',
            field=models.ForeignKey(to='ujc.Sexo'),
        ),
        migrations.AddField(
            model_name='delegado',
            name='casa',
            field=models.ForeignKey(to='ujc.Casa'),
        ),
        migrations.AddField(
            model_name='delegado',
            name='escolaridad',
            field=models.ForeignKey(to='ujc.Escolaridad'),
        ),
        migrations.AddField(
            model_name='delegado',
            name='limitacion',
            field=models.ForeignKey(to='ujc.Limitacion'),
        ),
        migrations.AddField(
            model_name='delegado',
            name='provincia',
            field=models.ForeignKey(to='ujc.Provincia'),
        ),
        migrations.AddField(
            model_name='delegado',
            name='sexo',
            field=models.ForeignKey(to='ujc.Sexo'),
        ),
    ]
