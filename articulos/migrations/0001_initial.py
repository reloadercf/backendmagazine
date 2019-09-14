# Generated by Django 2.2.4 on 2019-09-13 18:54

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
                ('imagen_destacada_uno', models.URLField()),
                ('redactado_por', models.CharField(blank=True, default='Equipo MX OPPORTUNITY', max_length=300, null=True)),
                ('status', models.CharField(choices=[('Publicado', 'Publicado'), ('No Publicado', 'No publicado')], default='Publicado', max_length=50)),
                ('cuerpo_uno', models.TextField()),
                ('imagen_destacada_dos', models.URLField()),
                ('cuerpo_dos', models.TextField(blank=True, null=True)),
                ('video_tipo', models.CharField(choices=[('youtube', 'youtube'), ('vimeo', 'vimeo'), ('sin video', 'sin video')], default='sin video', max_length=50)),
                ('urlvideo', models.URLField(blank=True, null=True)),
                ('llamada_accion_uno', models.CharField(choices=[('Contactar', 'Contactar'), ('Visitar', 'Visitar'), ('Compar', 'Comprar'), ('Llamar', 'Llamar'), ('Sinllamada', 'Sinllamada')], max_length=50)),
                ('imagen_llamada_uno', models.URLField()),
                ('llamada_per_uno', models.CharField(blank=True, max_length=50, null=True)),
                ('url_llamada_uno', models.TextField(blank=True, null=True)),
                ('llamada_accion_dos', models.CharField(choices=[('Contactar', 'Contactar'), ('Visitar', 'Visitar'), ('Compar', 'Comprar'), ('Llamar', 'Llamar'), ('Sinllamada', 'Sinllamada')], max_length=50)),
                ('imagen_llamada_dos', models.URLField()),
                ('llamada_per_dos', models.CharField(blank=True, max_length=50, null=True)),
                ('url_llamada_dos', models.TextField(blank=True, null=True)),
                ('cortesia_de', models.CharField(blank=True, max_length=300, null=True)),
                ('fecha_mostrada', models.DateField()),
                ('fecha_publicacion', models.DateTimeField()),
                ('fecha_fin', models.DateField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
