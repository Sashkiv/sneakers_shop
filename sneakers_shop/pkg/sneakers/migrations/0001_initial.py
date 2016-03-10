# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sneakers_shop.pkg.sneakers.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID',
                                        primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=255,
                                           verbose_name='Назва бренду')),
            ],
            options={
                'db_table': 'sneakers_brand',
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренди',
            },
        ),
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID',
                                        primary_key=True, auto_created=True)),
                ('model', models.CharField(max_length=255,
                                           verbose_name='Модель')),
                ('sex', models.PositiveSmallIntegerField(
                    db_index=True,
                    verbose_name='Стать',
                    default=0,
                    choices=[(0, 'Чоловічі'), (1, 'Жіночі')]
                )),
                ('size', models.SmallIntegerField(verbose_name='Розмір')),
                ('description', models.TextField(verbose_name='Опис')),
                ('is_ready', models.BooleanField(verbose_name='Опублікувати')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(verbose_name='Бренд',
                                            to='sneakers.Brand')),
            ],
            options={
                'db_table': 'sneakers_info',
                'verbose_name': 'Кросівки',
                'verbose_name_plural': 'Кросівки',
            },
        ),
        migrations.CreateModel(
            name='SneakersPhoto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID',
                                        primary_key=True, auto_created=True)),
                ('image', models.ImageField(
                    upload_to=sneakers_shop.pkg.sneakers.models.SneakersPhoto.
                    upload_path,
                    verbose_name='Зображення',
                    default='sneakers/without-photo.jpg')),
                ('is_ready', models.BooleanField(verbose_name='Опублікувати')),
                ('sneakers', models.ForeignKey(to='sneakers.Sneaker',
                                               verbose_name='Кросівки',
                                               related_name='sneakers_photo')),
            ],
            options={
                'db_table': 'sneakers_photo',
                'verbose_name': 'Зображення',
                'verbose_name_plural': 'Зображення',
            },
        ),
    ]
