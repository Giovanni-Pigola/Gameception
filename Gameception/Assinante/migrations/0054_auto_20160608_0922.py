# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-08 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0053_auto_20160606_2336'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoMidia',
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
