# Generated by Django 4.1.1 on 2022-10-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0012_filme_assistido_filme_classificacao_filme_genero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='classificacao',
            field=models.CharField(choices=[('L', 'Livre'), ('10', '10 anos'), ('14', '14 anos'), ('16', '16 anos'), ('18', '18 anos')], max_length=5),
        ),
        migrations.AlterField(
            model_name='filme',
            name='genero',
            field=models.CharField(choices=[('AC', 'Ação'), ('AV', 'Aventura'), ('CO', 'Comédia'), ('DO', 'Documentário'), ('DR', 'Drama'), ('FI', 'Ficção Científica'), ('MU', 'Musical'), ('RO', 'Romance'), ('SU', 'Suspense'), ('TE', 'Terror')], max_length=15),
        ),
    ]
