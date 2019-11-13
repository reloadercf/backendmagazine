# Generated by Django 2.1.3 on 2019-11-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regiones', '0001_initial'),
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revista',
            name='city',
        ),
        migrations.AddField(
            model_name='revista',
            name='city',
            field=models.ManyToManyField(to='regiones.Ciudad'),
        ),
        migrations.RemoveField(
            model_name='revista',
            name='country',
        ),
        migrations.AddField(
            model_name='revista',
            name='country',
            field=models.ManyToManyField(to='regiones.Region'),
        ),
        migrations.RemoveField(
            model_name='revista',
            name='state',
        ),
        migrations.AddField(
            model_name='revista',
            name='state',
            field=models.ManyToManyField(to='regiones.Subregion'),
        ),
    ]
