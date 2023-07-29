# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0018_embarazadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegado',
            name='sexo',
            field=models.CharField(max_length=30),
        ),
    ]
