# Generated by Django 4.1.2 on 2022-11-10 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0017_alter_filme_filme_criado_por'),
        ('autenticacao', '0004_remove_usuario_confirmar_senha'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
