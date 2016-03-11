# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sneakers_shop.pkg.sneakers.models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sneakersphoto',
            name='image',
            field=models.ImageField(
                verbose_name='Зображення',
                default='without-photo.jpg',
                upload_to=sneakers_shop.pkg.sneakers.models.SneakersPhoto.
                upload_path
            ),
        ),
    ]
