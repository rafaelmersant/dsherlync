# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descuento', models.IntegerField(default=0, blank=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_factura', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activa'), (b'I', b'Inactiva')])),
                ('impresa', models.CharField(default=b'N', max_length=1, choices=[(b'S', b'SI'), (b'N', b'NO')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(to='facturas.Factura'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detalle',
            name='producto',
            field=models.ForeignKey(to='productos.Producto'),
            preserve_default=True,
        ),
    ]
