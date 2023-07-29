# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0024_auto_20190701_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='delegado',
            name='limitacion',
            field=models.ForeignKey(to='ujc.Limitacion'),
        ),
    ]
