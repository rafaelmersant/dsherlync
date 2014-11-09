# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0011_auto_20141108_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 24, 4, 46, 47, 625174)),
        ),
    ]
