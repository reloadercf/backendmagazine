# Generated by Django 2.2.5 on 2019-09-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('activo', models.BooleanField()),
                ('razonsocial', models.CharField(max_length=200)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('numero_cuenta', models.IntegerField(blank=True, null=True)),
                ('iniciocontrato', models.DateField()),
                ('terminocontrato', models.DateField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('contrato', models.FileField(blank=True, null=True, upload_to='contratos')),
            ],
        ),
    ]
