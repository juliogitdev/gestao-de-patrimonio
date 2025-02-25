# Generated by Django 5.1.6 on 2025-02-22 21:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bem',
            old_name='numero_serie',
            new_name='rfid',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='data_movimentacao',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='local_destino',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='local_origem',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='movimentacao',
            name='rfid_id',
            field=models.CharField(default='desconhecido', max_length=100),
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='tipo',
            field=models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída')], max_length=7),
        ),
    ]
