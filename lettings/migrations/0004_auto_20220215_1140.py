# Generated by Django 3.0 on 2022-02-15 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0003_auto_20220215_1131'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='letting',
            table='lettings_letting',
        ),
    ]