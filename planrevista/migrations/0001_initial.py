# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-04 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('revista', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='revista.Revista')),
                ('fecha_inicio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Forma_Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('no_meses', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlanRevista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('no_usuarios', models.CharField(max_length=5)),
                ('no_patrocinadores', models.CharField(max_length=5)),
                ('no_publicaciones_mensual', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='contrato',
            name='forma_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pago_contrato', to='planrevista.Forma_Pago'),
        ),
    ]
