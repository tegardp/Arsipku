# Generated by Django 3.2.4 on 2021-06-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsip', '0009_tup_kategori'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tup',
            name='kategori',
            field=models.CharField(choices=[('Surat Permohonan TUP', 'Surat Permohonan TUP'), ('Surat Persetujuan TUP', 'Surat Persetujuan TUP')], max_length=200, null=True),
        ),
    ]
