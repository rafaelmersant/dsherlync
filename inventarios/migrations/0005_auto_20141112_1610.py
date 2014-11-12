# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0004_auto_20141108_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fecha_entrada',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
