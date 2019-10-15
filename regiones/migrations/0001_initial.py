# Generated by Django 2.2.6 on 2019-10-15 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ciudad', models.CharField(max_length=80)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estado_ciudad', to='regiones.Subregion')),
            ],
        ),
    ]