# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0017_auto_20190609_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embarazadas',
            fields=[
                ('delegado_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ujc.Delegado')),
                ('posibleFechaDeParto', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Embarazadas',
            },
            bases=('ujc.delegado',),
        ),
    ]
