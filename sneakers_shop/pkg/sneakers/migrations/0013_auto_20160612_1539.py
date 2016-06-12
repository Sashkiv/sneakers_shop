# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0012_auto_20160504_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promoinfo',
            options={'verbose_name': 'Акція. Оголошення', 'ordering': ['-modified'], 'verbose_name_plural': 'Акції та оголошення'},
        ),
        migrations.AddField(
            model_name='promoinfo',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата останнього оновлення', default=datetime.datetime(2016, 6, 12, 15, 39, 23, 755538, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
