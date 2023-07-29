# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0005_auto_20190605_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direccion', models.CharField(max_length=50)),
                ('cant_Delegados', models.IntegerField()),
                ('delegado', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Casas',
            },
        ),
    ]
