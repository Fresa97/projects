# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0007_auto_20190606_1136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Casa',
        ),
        migrations.DeleteModel(
            name='Casas',
        ),
        migrations.RemoveField(
            model_name='embarazadas',
            name='delegado',
        ),
        migrations.DeleteModel(
            name='Escolaridad',
        ),
        migrations.RemoveField(
            model_name='jefenucleo',
            name='integrante',
        ),
        migrations.DeleteModel(
            name='Provincia',
        ),
        migrations.DeleteModel(
            name='Delegado',
        ),
        migrations.DeleteModel(
            name='Embarazadas',
        ),
        migrations.DeleteModel(
            name='IntegrantesNucleo',
        ),
        migrations.DeleteModel(
            name='JefeNucleo',
        ),
    ]
