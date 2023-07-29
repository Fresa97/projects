# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0016_auto_20190608_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='embarazadas',
            name='delegado_ptr',
        ),
        migrations.DeleteModel(
            name='Embarazadas',
        ),
    ]
