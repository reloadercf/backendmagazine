# Generated by Django 2.1.3 on 2019-11-11 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('en_portada', models.BooleanField(default=False)),
                ('imagen', models.TextField()),
                ('redactado_por', models.CharField(blank=True, default='Equipo MX OPPORTUNITY', max_length=300, null=True)),
                ('publicado', models.BooleanField(default=False)),
                ('cortesia_de', models.CharField(blank=True, max_length=300, null=True)),
                ('fecha_publicacion', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
