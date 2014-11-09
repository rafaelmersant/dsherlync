# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
        ('inventarios', '0002_auto_20140920_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Existencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('tipo_movimiento', models.CharField(default=b'E', max_length=1, verbose_name=b'Tipo Movimiento', choices=[(b'E', b'Entrada'), (b'S', b'Salida')])),
                ('producto', models.ForeignKey(to='productos.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fecha_entrada',
            field=models.DateField(),
        ),
    ]
