# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0003_auto_20141112_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 27, 23, 32, 54, 365133)),
        ),
    ]
