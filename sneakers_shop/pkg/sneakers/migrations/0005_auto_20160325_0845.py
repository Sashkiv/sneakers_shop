# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0004_sneaker_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakerssize',
            name='size',
            field=models.FloatField(verbose_name='Розмір'),
        ),
    ]
