# Generated by Django 2.2.6 on 2019-10-15 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patrocinadores', '0001_initial'),
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrocinador',
            name='revista_pertenencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_origen', to='revista.Revista'),
        ),
    ]
