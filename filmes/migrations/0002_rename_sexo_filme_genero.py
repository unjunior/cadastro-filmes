# Generated by Django 4.1.1 on 2022-10-03 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='sexo',
            new_name='genero',
        ),
    ]
