# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '__first__'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(max_digits=8, decimal_places=2)),
                ('fecha_vence', models.DateTimeField(default=datetime.datetime(2014, 10, 5, 3, 17, 57, 655232))),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
