# Generated by Django 4.1.1 on 2022-10-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0008_alter_filme_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='classificacao',
            field=models.CharField(choices=[('livre', 'Livre'), ('10', '10 anos'), ('14', '14 anos'), ('16', '16 anos'), ('18', '18 anos')], max_length=5),
        ),
    ]
