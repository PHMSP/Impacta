# Generated by Django 3.2.18 on 2024-05-12 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adocao_cachorro', '0002_cachorro'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachorro',
            name='imagem_url',
            field=models.URLField(blank=True),
        ),
    ]
