<<<<<<< HEAD
# Generated by Django 2.1.3 on 2019-11-11 22:33
=======
# Generated by Django 2.1.3 on 2019-11-11 22:27
>>>>>>> origin/python

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revista', '0001_initial'),
        ('patrocinadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrocinador',
            name='revista_pertenencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pat_revista', to='revista.Revista'),
        ),
    ]
