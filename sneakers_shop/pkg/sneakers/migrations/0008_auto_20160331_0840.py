# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0007_auto_20160330_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sneakersphoto',
            old_name='is_ready',
            new_name='is_first',
        ),
        migrations.AlterField(
            model_name='promoinfo',
            name='subtitle',
            field=models.CharField(max_length=127,
                                   verbose_name='Підзаголовок', blank=True),
        ),
        migrations.AlterField(
            model_name='promoinfo',
            name='title',
            field=models.CharField(max_length=127,
                                   verbose_name='Заголовок', blank=True),
        ),
    ]
