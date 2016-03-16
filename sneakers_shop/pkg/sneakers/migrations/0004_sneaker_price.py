# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0003_auto_20160316_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneaker',
            name='price',
            field=models.IntegerField(verbose_name='Ціна', default=0),
        ),
    ]
