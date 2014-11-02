# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0006_auto_20141027_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 16, 21, 57, 38, 735053)),
        ),
    ]
