# Generated by Django 4.1 on 2022-10-07 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0003_alter_dosen_fakultas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='Fakultas',
            new_name='fakultas',
        ),
        migrations.RenameField(
            model_name='mahasiswa',
            old_name='Prodi',
            new_name='prodi',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='Fakultas',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='Prodi',
        ),
        migrations.AddField(
            model_name='dosen',
            name='id_fakultas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.fakultas'),
        ),
        migrations.AddField(
            model_name='dosen',
            name='id_prodi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.prodi'),
        ),
        migrations.AlterField(
            model_name='fakultas',
            name='id_fakultas',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prodi',
            name='id_prodi',
            field=models.IntegerField(),
        ),
    ]
