# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from sneakers_shop.pkg.sneakers.models import SneakersPhoto


def add_thumbs(apps, schema_migrations):
    for p in SneakersPhoto.objects.all():
        p.create_thumbs()
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0013_auto_20160612_1539'),
    ]

    operations = [
        migrations.RunPython(add_thumbs)
    ]
