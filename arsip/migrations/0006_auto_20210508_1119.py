# Generated by Django 3.1.7 on 2021-05-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arsip', '0005_auto_20210508_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dipa',
            name='uraian_dipa',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
