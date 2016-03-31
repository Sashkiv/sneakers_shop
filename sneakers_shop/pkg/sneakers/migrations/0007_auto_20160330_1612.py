# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0006_promoinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneaker',
            name='gender',
            field=models.PositiveSmallIntegerField(
                null=True,
                choices=[
                    (0, 'Чоловічі'), (1, 'Жіночі')
                ],
                db_index=True,
                verbose_name='Стать',
                default=0,
                blank=True),
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='model',
            field=models.CharField(verbose_name='Модель', null=True,
                                   blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='price',
            field=models.IntegerField(verbose_name='Ціна', null=True,
                                      default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='sneakersdescription',
            name='description',
            field=models.TextField(verbose_name='Опис', null=True,
                                   blank=True),
        ),
        migrations.AlterField(
            model_name='sneakerssize',
            name='size',
            field=models.FloatField(verbose_name='Розмір', null=True,
                                    blank=True),
        ),
    ]
