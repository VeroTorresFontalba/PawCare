# Generated by Django 4.2 on 2023-05-10 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_user_categoria_user_tipodeusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tipodeusuario',
            field=models.CharField(choices=[('CL', 'Cliente'), ('CU', 'Cuidador')], max_length=2),
        ),
    ]
