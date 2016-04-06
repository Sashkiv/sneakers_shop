# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0009_auto_20160402_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakersphoto',
            name='is_first',
            field=models.BooleanField(verbose_name='Основне зображення'),
        ),
    ]
