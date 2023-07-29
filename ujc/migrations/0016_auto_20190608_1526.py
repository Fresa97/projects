# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0015_auto_20190608_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='embarazadas',
            name='delegado',
        ),
        migrations.AddField(
            model_name='embarazadas',
            name='delegado_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to='ujc.Delegado'),
            preserve_default=False,
        ),
    ]
