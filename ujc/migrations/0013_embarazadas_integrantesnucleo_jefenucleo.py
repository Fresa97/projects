# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0012_delegado'),
    ]

    operations = [
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
    ]
