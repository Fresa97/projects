# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ujc', '0008_auto_20190606_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreProvincia', models.CharField(max_length=30)),
                ('primersecretario', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
            },
        ),
    ]
