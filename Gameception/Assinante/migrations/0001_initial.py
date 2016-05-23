# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assinante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.IntegerField()),
                ('nome', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('rua', models.CharField(max_length=200)),
                ('numeroRua', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('CEP', models.IntegerField()),
            ],
        ),
    ]
