# Generated by Django 4.1 on 2022-10-05 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_fakultas_alter_dosen_fakultas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='Fakultas',
        ),
        migrations.DeleteModel(
            name='Mahasiswa',
        ),
        migrations.DeleteModel(
            name='Tendik',
        ),
        migrations.DeleteModel(
            name='Dosen',
        ),
        migrations.DeleteModel(
            name='Fakultas',
        ),
    ]
