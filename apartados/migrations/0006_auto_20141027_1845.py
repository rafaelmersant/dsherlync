# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('apartados', '0005_auto_20141025_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 11, 18, 45, 6, 27679)),
        ),
    ]
