from django.contrib import admin
from django.contrib.auth.models import Group

from sneakers_shop.pkg.sneakers.models import Brand, Sneaker, SneakersPhoto, \
    SneakersDescription, SneakersSize


class SneakersPhotoInlineAdmin(admin.TabularInline):
    model = SneakersPhoto
    extra = 1


class SneakersDescriptionInlineAdmin(admin.TabularInline):
    model = SneakersDescription
    extra = 1


class SneakersSizeInlineAdmin(admin.TabularInline):
    model = SneakersSize
    extra = 1


class SneakersAdmin(admin.ModelAdmin):
    class Meta:
        model = Sneaker

    list_display = ('__str__', 'gender', 'date_update', )
    list_filter = ('is_ready', 'gender', 'brand', )
    date_hierarchy = 'date_update'
    inlines = [
        SneakersSizeInlineAdmin,
        SneakersDescriptionInlineAdmin,
        SneakersPhotoInlineAdmin,
    ]


admin.site.register(Brand)
admin.site.register(Sneaker, SneakersAdmin)
admin.site.unregister(Group)
