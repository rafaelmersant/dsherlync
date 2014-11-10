# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0014_auto_20141109_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartado',
            name='no_apartado',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 25, 3, 15, 35, 893446)),
        ),
    ]
