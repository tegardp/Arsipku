# Generated by Django 3.2.4 on 2021-06-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsip', '0008_auto_20210610_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='tup',
            name='kategori',
            field=models.CharField(choices=[('Surat Permohonan TUP', 'Surat Permohonan TUP'), ('Surat Persetujuan TUP', 'Surat Persetujuan TUP'), ('Laporan Kegiatan', 'Laporan Kegiatan')], max_length=200, null=True),
        ),
    ]
