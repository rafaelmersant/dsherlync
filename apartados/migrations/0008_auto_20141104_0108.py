# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0007_auto_20141101_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 19, 1, 8, 9, 276427)),
        ),
    ]
