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

    GENDER = (
        (MALE, _('Чоловічі')),
        (FEMALE, _('Жіночі')),
    )

    brand = models.ForeignKey(Brand, verbose_name=_('Бренд'))
    model = models.CharField(max_length=255, verbose_name=_('Модель'))
    gender = models.PositiveSmallIntegerField(
        choices=GENDER, default=MALE, db_index=True, verbose_name=_('Стать')
    )
    price = models.IntegerField(default=0, verbose_name=_('Ціна'))
    is_ready = models.BooleanField(verbose_name=_('Опублікувати'))
    date_add = models.DateTimeField(auto_now_add=True,
                                    verbose_name=_('Дата додання'))
    date_update = models.DateTimeField(
        auto_now=True, verbose_name=_('Дата останнього оновлення')
    )

    def __str__(self):
        return '{} | {}'.format(self.brand, self.model)


class SneakersDescription(models.Model):
    class Meta:
        db_table = 'sneakers_description'
        verbose_name = _('Опис')
        verbose_name_plural = _('Описи')

    UKRAINIAN = 'uk'
    RUSSIAN = 'ru'

    LANGUAGES = (
        (UKRAINIAN, _('Українська')),
        (RUSSIAN, _('Російська')),
    )

    sneakers = models.ForeignKey(
        Sneaker,
        related_name='sneakers_description',
        verbose_name=_('Кросівки')
    )
    description = models.TextField(verbose_name=_('Опис'))
    language = models.CharField(
        max_length=7,
        choices=LANGUAGES,
        default=UKRAINIAN,
        db_index=True,
        verbose_name=_('Мова')
    )

    def __str__(self):
        return '{} | Опис (мова: {})'.format(self.sneakers, self.language)


class SneakersSize(models.Model):
    class Meta:
        db_table = 'sneakers_size'
        verbose_name = _('Розмір')
        verbose_name_plural = _('Розміри')

    sneakers = models.ForeignKey(Sneaker, related_name='sneakers_size')
    size = models.FloatField(verbose_name=_('Розмір'))

    def __str__(self):
        return '{} | розмір: {}'.format(self.sneakers, self.size)


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
