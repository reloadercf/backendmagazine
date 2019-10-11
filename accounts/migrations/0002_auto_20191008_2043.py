# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-08 20:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('revista', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='revista',
            field=models.ManyToManyField(to='revista.Revista'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tipo_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revista_perfil', to='accounts.TipoUsuario'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
