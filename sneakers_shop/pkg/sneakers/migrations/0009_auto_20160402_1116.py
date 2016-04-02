# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0008_auto_20160331_0840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False,
                                        primary_key=True, verbose_name='ID')),
                ('contact_info', models.CharField(
                    verbose_name='Контактна інформація',
                    max_length=63)),
                ('comment', models.TextField(
                    verbose_name='Коментар',
                    blank=True, max_length=1023
                )),
                ('date_order', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'db_table': 'sneakers_order',
            },
        ),
        migrations.AlterField(
            model_name='sneaker',
            name='gender',
            field=models.PositiveSmallIntegerField(
                db_index=True,
                null=True,
                choices=[(0, 'Чоловічі'), (1, 'Жіночі'), (2, 'Для будь-кого')],
                blank=True,
                verbose_name='Стать',
                default=0
            ),
        ),
        migrations.AddField(
            model_name='order',
            name='sneakers',
            field=models.ForeignKey(verbose_name='Кросівки',
                                    to='sneakers.Sneaker'),
        ),
    ]
