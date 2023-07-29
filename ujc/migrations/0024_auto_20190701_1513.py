# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0023_auto_20190627_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embarazadas',
            name='posibleFechaDeParto',
            field=models.DateField(),
        ),
    ]
