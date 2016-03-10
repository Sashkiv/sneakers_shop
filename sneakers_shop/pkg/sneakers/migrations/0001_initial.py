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
                ('id', models.AutoField(auto_created=True, serialize=False,
                                        verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Назва бренду',
                                           max_length=255)),
            ],
            options={
                'verbose_name': 'Бренд',
                'db_table': 'sneakers_brand',
                'verbose_name_plural': 'Бренди',
            },
        ),
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False,
                                        verbose_name='ID', primary_key=True)),
                ('model', models.CharField(verbose_name='Модель',
                                           max_length=255)),
                ('sex', models.PositiveSmallIntegerField(
                    default=0,
                    choices=[(0, 'Чоловічі'), (1, 'Жіночі')],
                    db_index=True,
                    verbose_name='Стать'
                )),
                ('size', models.SmallIntegerField(verbose_name='Розмір')),
                ('description', models.TextField(verbose_name='Опис')),
                ('is_ready', models.BooleanField(verbose_name='Опублікувати')),
                ('brand', models.ForeignKey(verbose_name='Бренд',
                                            to='sneakers.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='SneakersPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False,
                                        verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(
                    default='sneakers/without-photo.jpg',
                    upload_to=sneakers_shop.pkg.sneakers.models.SneakersPhoto.
                            upload_path,
                    verbose_name='Зображення'
                )),
                ('is_ready', models.BooleanField(verbose_name='Опублікувати')),
                ('sneakers', models.ForeignKey(
                    to='sneakers.Sneaker',
                    related_name='sneakers_photo',
                    verbose_name='Кросівки'
                )),
            ],
            options={
                'verbose_name': 'Зображення',
                'db_table': 'sneakers_photo',
                'verbose_name_plural': 'Зображення',
            },
        ),
    ]
