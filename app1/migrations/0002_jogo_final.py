# Generated by Django 5.1 on 2024-09-01 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo_final',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_nome', models.CharField(max_length=300)),
                ('usuario_senha', models.CharField(max_length=70)),
                ('dinheiro', models.IntegerField(default=0)),
                ('tempo', models.IntegerField(default=0)),
                ('inimigos_derrotados', models.IntegerField(default=0)),
            ],
        ),
    ]
