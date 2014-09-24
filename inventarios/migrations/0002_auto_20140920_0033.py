# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='tipo_inv',
            field=models.CharField(default=b'E', max_length=1, verbose_name=b'Tipo de Inventario', choices=[(b'E', b'Entrada'), (b'S', b'Salida')]),
        ),
    ]
