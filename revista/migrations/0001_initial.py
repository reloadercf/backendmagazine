# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-04 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regiones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_revista', models.CharField(max_length=80)),
                ('logo', models.URLField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_ciudad', to='regiones.Ciudad')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_pais', to='regiones.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_subcategoria', models.CharField(max_length=80)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_sub', to='revista.Categorias')),
            ],
        ),
    ]
