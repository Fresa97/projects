# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0021_auto_20190627_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='JefeNucleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ocupacion', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('integrante', models.OneToOneField(to='ujc.IntegrantesNucleo')),
            ],
            options={
                'verbose_name_plural': 'Jefe de Nucleo',
            },
        ),
    ]
