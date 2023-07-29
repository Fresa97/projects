# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0002_auto_20190605_1715'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Casa',
        ),
    ]
