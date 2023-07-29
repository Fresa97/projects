# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0006_casas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casas',
            name='delegado',
        ),
        migrations.RemoveField(
            model_name='delegado',
            name='escolaridad',
        ),
        migrations.RemoveField(
            model_name='delegado',
            name='provincia',
        ),
    ]
