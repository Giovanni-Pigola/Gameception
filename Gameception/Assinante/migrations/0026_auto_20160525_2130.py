# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0025_auto_20160525_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogo',
            name='listaGeneros',
            field=models.ManyToManyField(to='Assinante.Genero'),
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
