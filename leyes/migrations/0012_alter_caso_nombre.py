# Generated by Django 4.2.4 on 2023-08-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leyes', '0011_alter_caso_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caso',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]