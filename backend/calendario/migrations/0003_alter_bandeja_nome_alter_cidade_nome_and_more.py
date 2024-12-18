# Generated by Django 5.1.2 on 2024-12-08 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0002_cidade_evento_plantio_dicas_plantio_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandeja',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cultura',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='plantio',
            name='bandeja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendario.bandeja'),
        ),
        migrations.AlterField(
            model_name='plantio',
            name='cultura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calendario.cultura'),
        ),
    ]
