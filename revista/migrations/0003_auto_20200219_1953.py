# Generated by Django 3.0.3 on 2020-02-19 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0002_auto_20191120_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='icono',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='Icon',
        ),
    ]
