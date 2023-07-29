# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0014_integrantesnucleo_casa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantesnucleo',
            name='casa',
            field=models.ForeignKey(to='ujc.Casa'),
        ),
    ]
