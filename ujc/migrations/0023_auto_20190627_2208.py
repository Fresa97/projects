# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0022_jefenucleo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embarazadas',
            name='posibleFechaDeParto',
            field=models.DateTimeField(),
        ),
    ]
