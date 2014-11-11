# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0015_auto_20141110_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='estatus',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'X', b'Anulado'), (b'C', b'Completado')]),
        ),
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 26, 5, 6, 33, 509299)),
        ),
    ]
