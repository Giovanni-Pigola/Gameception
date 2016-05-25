# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 00:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0006_sistop_sistop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.IntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='assinante',
            name='dAssinatura',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.DadosAssinatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assinante',
            name='dBanco',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.DadosBancarios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assinante',
            name='endAssinatura',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.EnderecoAssinatura'),
            preserve_default=False,
        ),
    ]