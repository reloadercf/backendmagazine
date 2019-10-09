# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-08 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_pais', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Subregion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(max_length=80)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pais_estado', to='regiones.Region')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estado_ciudad', to='regiones.Subregion'),
        ),
    ]
