# Generated by Django 2.1.3 on 2019-11-13 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regiones', '0001_initial'),
        ('revista', '0002_auto_20191113_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revista',
            name='city',
        ),
        migrations.AddField(
            model_name='revista',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='revista_plan', to='regiones.Ciudad'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='revista',
            name='country',
        ),
        migrations.AddField(
            model_name='revista',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='revista_plan', to='regiones.Region'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='revista',
            name='state',
        ),
        migrations.AddField(
            model_name='revista',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='revista_plan', to='regiones.Subregion'),
            preserve_default=False,
        ),
    ]