# Generated by Django 2.2.4 on 2019-09-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('razonsocial', models.CharField(max_length=200)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
