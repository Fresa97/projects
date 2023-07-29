# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=50)),
                ('cant_Delegdos', models.IntegerField()),
                ('delegado', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Casa',
            },
        ),
        migrations.RemoveField(
            model_name='jefenucleo',
            name='ocupacion',
        ),
        migrations.RemoveField(
            model_name='jefenucleo',
            name='sexo',
        ),
    ]
