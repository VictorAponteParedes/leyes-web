# Generated by Django 4.2.4 on 2023-08-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leyes', '0013_caso_juzgado_alter_caso_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='juzgado',
            field=models.CharField(default='', help_text='Ingrese el nombre del Juzgado', max_length=100),
        ),
    ]
