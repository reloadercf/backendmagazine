# Generated by Django 2.2.6 on 2019-11-05 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forma_Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('no_meses', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PlanRevista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('no_usuarios', models.CharField(max_length=5)),
                ('no_patrocinadores', models.CharField(max_length=5)),
                ('no_publicaciones_mensual', models.CharField(max_length=5)),
                ('costo', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pago_contrato', to='planrevista.Forma_Pago')),
            ],
        ),
    ]
