from django.contrib import admin
from django.contrib.auth.models import Group

from sneakers_shop.pkg.sneakers.models import Brand, Sneaker, SneakersPhoto, \
    SneakersDescription, SneakersSize, PromoInfo, Order


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


class OrderAdmin(admin.ModelAdmin):
    class Meta:
        model = Order

    def link_to_sneakers_in_admin(self, obj):
        return '<a target="_blank" href="/admin/sneakers/sneaker/{}/">' \
               'Переглянути кросівки на сторінці адміністратора</a>'\
            .format(obj.sneakers.id)

    link_to_sneakers_in_admin.allow_tags = True
    link_to_sneakers_in_admin.short_description = 'Кросівки'

    def link_to_sneakers(self, obj):
        return '<a target="_blank" href="/sneakers/{}/">' \
               'Переглянути кросівки</a>'.format(obj.sneakers.id)

    link_to_sneakers.allow_tags = True
    link_to_sneakers.short_description = 'Кросівки'
    readonly_fields = ('sneakers', 'contact_info', 'comment',
                       'link_to_sneakers', 'link_to_sneakers_in_admin')
    date_hierarchy = 'date_order'


admin.site.register(Brand)
admin.site.register(PromoInfo)
admin.site.register(Order, OrderAdmin)
admin.site.register(Sneaker, SneakersAdmin)
admin.site.unregister(Group)
