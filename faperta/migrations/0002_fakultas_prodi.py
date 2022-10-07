# Generated by Django 4.1 on 2022-10-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fakultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_fakultas', models.IntegerField(max_length=50)),
                ('nama_fakultas', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_prodi', models.IntegerField(max_length=50)),
                ('nama_prodi', models.CharField(max_length=200)),
            ],
        ),
    ]
