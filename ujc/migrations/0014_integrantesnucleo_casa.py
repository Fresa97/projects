# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0013_embarazadas_integrantesnucleo_jefenucleo'),
    ]

    operations = [
        migrations.AddField(
            model_name='integrantesnucleo',
            name='casa',
            field=models.ForeignKey(default=1, to='ujc.Casa'),
        ),
    ]
