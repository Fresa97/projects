# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0019_auto_20190609_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegado',
            name='sexo',
            field=models.CharField(max_length=10),
        ),
    ]
