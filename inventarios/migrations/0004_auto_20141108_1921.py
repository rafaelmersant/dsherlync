# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0003_auto_20141107_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento',
            name='tipo_movimiento',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='fecha_movimiento',
            field=models.DateField(default=datetime.date(2014, 11, 8), auto_now_add=True),
            preserve_default=False,
        ),
    ]
