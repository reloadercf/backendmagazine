# Generated by Django 2.1.3 on 2019-11-11 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Imagen', 'Imagen'), ('Texto', 'Texto'), ('Video', 'Video'), ('Publicidad', 'Publicidad')], max_length=200)),
                ('recurso', models.TextField()),
                ('alt', models.TextField(blank=True, null=True)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='con_art', to='articulos.Articulo')),
            ],
        ),
    ]