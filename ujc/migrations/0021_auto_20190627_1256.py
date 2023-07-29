# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0020_auto_20190622_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jefenucleo',
            name='integrante',
        ),
        migrations.DeleteModel(
            name='JefeNucleo',
        ),
    ]
