# Generated by Django 2.1.3 on 2019-11-11 22:33

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
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('relacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_revista', models.CharField(max_length=100, unique=True)),
                ('logo', models.URLField(blank=True, max_length=300, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revista_ciudad', to='regiones.Ciudad')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revista_pais', to='regiones.Region')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_plan', to='planrevista.PlanRevista')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revista_estado', to='regiones.Subregion')),
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
        migrations.AddField(
            model_name='categorias',
            name='icono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_icon', to='revista.Icon'),
        ),
        migrations.AddField(
            model_name='categorias',
            name='revista_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_revista', to='revista.Revista'),
        ),
    ]
