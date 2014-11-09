# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0012_auto_20141109_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartado',
            name='estatus',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'X', b'Anulado')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 24, 4, 49, 23, 735362)),
        ),
    ]
