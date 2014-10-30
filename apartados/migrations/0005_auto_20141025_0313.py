# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0004_auto_20141001_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 9, 3, 13, 36, 687216)),
        ),
    ]
