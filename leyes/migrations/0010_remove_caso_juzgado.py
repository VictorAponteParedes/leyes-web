# Generated by Django 4.2.4 on 2023-08-16 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leyes', '0009_rename_ano_caso_fecha_alter_caso_juzgado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caso',
            name='juzgado',
        ),
    ]
