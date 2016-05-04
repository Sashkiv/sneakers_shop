# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from sneakers_shop.pkg.sneakers.models import SneakersPhoto


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0010_auto_20160406_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='sneakersphoto',
            name='thumbs',
            field=models.ImageField(
                default=SneakersPhoto.DEFAULT_IMG,
                verbose_name='Мініатюра зображення',
                upload_to=SneakersPhoto.upload_path),
        )
    ]
