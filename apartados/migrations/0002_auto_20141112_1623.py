# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonocliente',
            name='ap',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 27, 16, 23, 30, 276275)),
        ),
    ]
