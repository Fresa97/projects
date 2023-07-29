# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0011_casa'),
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
                ('casa', models.ForeignKey(to='ujc.Casa')),
                ('escolaridad', models.ForeignKey(to='ujc.Escolaridad')),
                ('provincia', models.ForeignKey(to='ujc.Provincia')),
            ],
            options={
                'verbose_name_plural': 'Delegados',
            },
        ),
    ]
