# Generated by Django 2.2.4 on 2019-09-13 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('regiones', '0001_initial'),
        ('planrevista', '0001_initial'),
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
            name='Subcategorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_subcategoria', models.CharField(max_length=80)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_sub', to='revista.Categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_revista', models.CharField(max_length=80)),
                ('logo', models.URLField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_estado', to='regiones.Subregion')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_pais', to='regiones.Region')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_plan', to='planrevista.PlanRevista')),
            ],
        ),
        migrations.AddField(
            model_name='categorias',
            name='revista_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_revista', to='revista.Revista'),
        ),
    ]
