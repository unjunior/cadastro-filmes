# Generated by Django 4.1.1 on 2022-10-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0007_remove_filme_assistido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.CharField(choices=[('acao', 'Ação'), ('aventura', 'Aventura'), ('comedia', 'Comédia'), ('documentario', 'Documentário'), ('drama', 'Drama'), ('ficcao', 'Ficção Científica'), ('musical', 'Musical'), ('romance', 'Romance'), ('suspense', 'Suspense'), ('terror', 'Terror')], max_length=15),
        ),
    ]
