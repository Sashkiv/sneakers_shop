from django.contrib import admin
from django.contrib.auth.models import Group

from sneakers_shop.pkg.sneakers.models import Brand, Sneaker, SneakersPhoto


class SneakersPhotoInlineAdmin(admin.StackedInline):
    model = SneakersPhoto


class SneakersAdmin(admin.ModelAdmin):
    class Meta:
        model = Sneaker

    list_display = ('__str__', 'sex', 'size', 'date_update', )
    list_filter = ('is_ready', 'sex', 'brand', 'size', )
    date_hierarchy = 'date_update'
    inlines = [SneakersPhotoInlineAdmin, ]


admin.site.register(Brand)
admin.site.register(Sneaker, SneakersAdmin)
admin.site.unregister(Group)
