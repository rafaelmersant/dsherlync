# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('apartados', '0013_auto_20141109_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbonoCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abono', models.DecimalField(max_digits=8, decimal_places=2)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
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
        migrations.AlterField(
            model_name='apartado',
            name='fecha_vence',
            field=models.DateField(default=datetime.datetime(2014, 11, 24, 5, 20, 19, 847405)),
        ),
        migrations.AlterField(
            model_name='apartado',
            name='precio',
            field=models.DecimalField(max_digits=8, decimal_places=2, blank=True),
        ),
    ]
