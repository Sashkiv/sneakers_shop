import random

from django.db import models
from django.utils.translation import ugettext_lazy as _

from sneakers_shop.pkg.sneakers.utils import random_string


class Brand(models.Model):
    class Meta:
        db_table = 'sneakers_brand'
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренди')

    title = models.CharField(max_length=255, verbose_name=_('Назва бренду'))

    def __str__(self):
        return self.title


class Sneaker(models.Model):
    class Meta:
        db_table = 'sneakers_info'
        verbose_name = _('Кросівки')
        verbose_name_plural = _('Кросівки')

    MALE = 0x00
    FEMALE = 0x01

    SEX = (
        (MALE, _('Чоловічі')),
        (FEMALE, _('Жіночі')),
    )

    brand = models.ForeignKey(Brand, verbose_name=_('Бренд'))
    model = models.CharField(max_length=255, verbose_name=_('Модель'))
    sex = models.PositiveSmallIntegerField(
        choices=SEX, default=MALE, db_index=True, verbose_name=_('Стать')
    )
    size = models.SmallIntegerField(verbose_name=_('Розмір'))
    description = models.TextField(verbose_name=_('Опис'))
    is_ready = models.BooleanField(verbose_name=_('Опублікувати'))
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} | {}'.format(self.brand, self.model)


class SneakersPhoto(models.Model):
    class Meta:
        db_table = 'sneakers_photo'
        verbose_name = _('Зображення')
        verbose_name_plural = _('Зображення')

    DEFAULT_IMG = 'without-photo.jpg'

    def upload_path(self, filename):
        name = random_string(size=12)
        ext = filename.split('.')[-1]
        self.filename = "tmp_%s.%s" % (name, ext)
        url = "sneakers/%s/%s" % (
            random.randint(1, 25),
            self.filename
        )
        return url

    sneakers = models.ForeignKey(Sneaker, verbose_name=_('Кросівки'),
                                 related_name='sneakers_photo', db_index=True)
    image = models.ImageField(upload_to=upload_path, default=DEFAULT_IMG,
                              verbose_name=_('Зображення'))
    is_ready = models.BooleanField(verbose_name=_('Опублікувати'))

    def __str__(self):
        return '{} | photo | {}'.format(self.sneakers, self.pk)
