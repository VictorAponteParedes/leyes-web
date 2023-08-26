# Generated by Django 4.2.4 on 2023-08-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leyes', '0018_caso_foto_perfil_cliente_foto_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='abogado',
            name='descripcion',
            field=models.TextField(blank=True, default='descripcion', help_text='Experiencia, estudio, idioma, certificaciones, etc.', null=True),
        ),
        migrations.AddField(
            model_name='abogado',
            name='especialidad',
            field=models.CharField(choices=[('laboral', 'Laboral'), ('civil y comercial', 'Civil y Comercial'), ('administrativo', 'Administrativo'), ('penal', 'Penal'), ('niñez y adolecencia', 'Niñez y Adolecencia')], default='laboral', max_length=20),
        ),
        migrations.AlterField(
            model_name='abogado',
            name='edad',
            field=models.IntegerField(blank=True, default=20, help_text='Ingrese su edad', null=True, verbose_name='Edad'),
        ),
    ]
