# Generated by Django 4.2.4 on 2023-08-17 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leyes', '0014_alter_caso_juzgado'),
    ]

    operations = [
        migrations.AddField(
            model_name='caso',
            name='materia',
            field=models.CharField(choices=[('laboral', 'Laboral'), ('civil y comercial', 'Civil y Comercial'), ('administrativo', 'Administrativo'), ('penal', 'Penal'), ('niñez y adolecencia', 'Niñez y Adolecencia')], default='laboral', max_length=20),
        ),
    ]
