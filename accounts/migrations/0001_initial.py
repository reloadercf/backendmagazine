<<<<<<< HEAD
# Generated by Django 2.2.6 on 2019-10-11 20:04
=======
# Generated by Django 2.2.4 on 2019-10-11 20:25
>>>>>>> 4d04a9e2b5c18e96683b6378502bddbcda0215de

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.URLField(blank=True, max_length=300, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'permissions': (('Administrador', 'Administrador'), ('Patrocinador', 'Patrocinador'), ('Editor', 'Editor'), ('Admin_Jr', 'Administrador Junior')),
            },
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
    ]
