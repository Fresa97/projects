# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0004_casa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casa',
            old_name='cantD',
            new_name='cantDelegados',
        ),
    ]
