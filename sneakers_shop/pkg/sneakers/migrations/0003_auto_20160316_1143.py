# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('sneakers', '0002_auto_20160314_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='SneakersDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False,
                                        primary_key=True, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Опис')),
                ('language',
                 models.CharField(db_index=True, max_length=7, default='uk',
                                  choices=[('uk', 'Українська'),
                                           ('ru', 'Російська')],
                                  verbose_name='Мова')),
            ],
            options={
                'verbose_name': 'Опис',
                'db_table': 'sneakers_description',
                'verbose_name_plural': 'Описи',
            },
        ),
        migrations.CreateModel(
            name='SneakersSize',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False,
                                        primary_key=True, verbose_name='ID')),
                ('size', models.SmallIntegerField(verbose_name='Розмір')),
            ],
            options={
                'verbose_name': 'Розмір',
                'db_table': 'sneakers_size',
                'verbose_name_plural': 'Розміри',
            },
        ),
        migrations.RenameField(
            model_name='sneaker',
            old_name='sex',
            new_name='gender',
        ),
        migrations.RemoveField(
            model_name='sneaker',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sneaker',
            name='size',
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='date_add',
            field=models.DateTimeField(verbose_name='Дата додання',
                                       auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='date_update',
            field=models.DateTimeField(
                verbose_name='Дата останнього оновлення',
                auto_now=True
            ),
        ),
        migrations.AddField(
            model_name='sneakerssize',
            name='sneakers',
            field=models.ForeignKey(to='sneakers.Sneaker',
                                    related_name='sneakers_size'),
        ),
        migrations.AddField(
            model_name='sneakersdescription',
            name='sneakers',
            field=models.ForeignKey(to='sneakers.Sneaker',
                                    related_name='sneakers_description',
                                    verbose_name='Кросівки'),
        ),
    ]
