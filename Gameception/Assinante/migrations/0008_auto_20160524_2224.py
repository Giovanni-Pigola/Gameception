# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0007_auto_20160524_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaveDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Processadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proc', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
        migrations.AddField(
            model_name='dadosassinatura',
            name='processador',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.Processadores'),
            preserve_default=False,
        ),
    ]
