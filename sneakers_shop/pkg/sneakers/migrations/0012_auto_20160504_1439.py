# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from sneakers_shop.pkg.sneakers.models import SneakersPhoto


def add_thumbs(apps, schema_editor):

    for img in SneakersPhoto.objects.all():
        img.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0011_add_thumbs'),
    ]

    operations = [
        migrations.RunPython(add_thumbs, lambda x, y: None)
    ]
