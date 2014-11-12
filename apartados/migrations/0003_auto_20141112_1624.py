# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0002_auto_20141112_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonocliente',
            name='estatus',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'X', b'Anulado'), (b'C', b'Completado')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abonocliente',
            name='ap',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 27, 16, 24, 46, 965527)),
        ),
    ]
