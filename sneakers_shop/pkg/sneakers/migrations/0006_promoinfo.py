# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sneakers_shop.pkg.sneakers.models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0005_auto_20160325_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromoInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True,
                                        primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=127,
                                           verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=127,
                                              verbose_name='Підзаголовок')),
                ('url', models.CharField(max_length=127,
                                         verbose_name='Посилання')),
                ('style', models.TextField(max_length=2047,
                                           verbose_name='Стилі', blank=True)),
                ('image', models.ImageField(
                    upload_to=sneakers_shop.pkg.sneakers.models.PromoInfo.
                    upload_path,
                    default='coverages/no-cover.jpg',
                    verbose_name='Фон'
                )),
                ('is_ready', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'sneakers_promo',
                'verbose_name': 'Акція. Оголошення',
                'verbose_name_plural': 'Акції та оголошення',
            },
        ),
    ]
