import random

from django.db import models

from sneakers_shop.pkg.sneakers.utils import random_string


class Brand(models.Model):
    class Meta:
        db_table = 'sneakers_brand'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

    title = models.CharField(max_length=255, verbose_name='Назва бренду')


class Sneaker(models.Model):
    class Model:
        db_table = 'sneakers_info'
        verbose_name = 'Кросівки'
        verbose_name_plural = 'Кросівки'

    MALE = 0x00
    FEMALE = 0x01

    SEX = (
        (MALE, 'Чоловічі'),
        (FEMALE, 'Жіночі'),
    )

    brand = models.ForeignKey(Brand, verbose_name='Бренд')
    model = models.CharField(max_length=255, verbose_name='Модель')
    sex = models.PositiveSmallIntegerField(
        choices=SEX, default=MALE, db_index=True, verbose_name='Стать'
    )
    size = models.SmallIntegerField(verbose_name='Розмір')
    description = models.TextField(verbose_name='Опис')
    is_ready = models.BooleanField(verbose_name='Опублікувати')


class SneakersPhoto(models.Model):
    class Meta:
        db_table = 'sneakers_photo'
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    DEFAULT_IMG = 'sneakers/without-photo.jpg'

    def upload_path(self, filename):
        name = random_string(size=12)
        ext = filename.split('.')[-1]
        self.filename = "tmp_%s.%s" % (name, ext)
        url = "sneakers/%s/%s" % (
            random.randint(1, 25),
            self.filename
        )
        return url

    sneakers = models.ForeignKey(Sneaker, verbose_name='Кросівки',
                                 related_name='sneakers_photo')
    image = models.ImageField(upload_to=upload_path, default=DEFAULT_IMG,
                              verbose_name='Зображення')
    is_ready = models.BooleanField(verbose_name='Опублікувати')
