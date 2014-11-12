# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('productos', '0002_auto_20141112_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abono', models.DecimalField(max_digits=8, decimal_places=2)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('ap', models.IntegerField()),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Apartado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_apartado', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(max_digits=8, decimal_places=2, blank=True)),
                ('fecha_vence', models.DateField(default=datetime.datetime(2014, 11, 27, 16, 22, 4, 132580))),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'X', b'Anulado'), (b'C', b'Completado')])),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeudaCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deuda', models.DecimalField(max_digits=8, decimal_places=2)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
