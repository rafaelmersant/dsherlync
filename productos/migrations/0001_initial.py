# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clasificaciones', '__first__'),
        ('grupos', '__first__'),
        ('departamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.DecimalField(max_digits=12, decimal_places=2, blank=True)),
                ('clasificacion', models.ForeignKey(to='clasificaciones.Clasificacion')),
                ('departamento', models.ForeignKey(to='departamentos.Departamento')),
                ('grupo', models.ForeignKey(related_name=b'grupos_rel', to='grupos.Grupo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
