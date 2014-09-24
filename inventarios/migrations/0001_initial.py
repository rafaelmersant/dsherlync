# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_entrada', models.DateField(auto_now_add=True)),
                ('tipo_inv', models.CharField(default=b'E', max_length=1, choices=[(b'E', b'Entrada'), (b'S', b'Salida')])),
                ('descripcion_salida', models.CharField(max_length=255, verbose_name=b'Descripci\xc3\xb3n de Salida', blank=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
