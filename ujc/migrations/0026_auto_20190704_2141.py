# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0025_auto_20190704_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegado',
            name='casa',
        ),
        migrations.RemoveField(
            model_name='delegado',
            name='escolaridad',
        ),
        migrations.RemoveField(
            model_name='delegado',
            name='limitacion',
        ),
        migrations.RemoveField(
            model_name='delegado',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='embarazadas',
            name='delegado_ptr',
        ),
        migrations.RemoveField(
            model_name='integrantesnucleo',
            name='casa',
        ),
        migrations.RemoveField(
            model_name='jefenucleo',
            name='integrante',
        ),
        migrations.DeleteModel(
            name='Sexo',
        ),
        migrations.DeleteModel(
            name='Casa',
        ),
        migrations.DeleteModel(
            name='Delegado',
        ),
        migrations.DeleteModel(
            name='Embarazadas',
        ),
        migrations.DeleteModel(
            name='Escolaridad',
        ),
        migrations.DeleteModel(
            name='IntegrantesNucleo',
        ),
        migrations.DeleteModel(
            name='JefeNucleo',
        ),
        migrations.DeleteModel(
            name='Limitacion',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
    ]
