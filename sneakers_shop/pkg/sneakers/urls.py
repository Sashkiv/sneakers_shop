from django.conf.urls import url

from sneakers_shop.pkg.sneakers.views import SneakersCatalogView, \
    SneakersDetailView, SneakersListView, PromoListView

urlpatterns = [
    url(r'^promo_list/', PromoListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/', SneakersDetailView.as_view()),
    url(r'^list/', SneakersListView.as_view()),
    url(r'^$', SneakersCatalogView.as_view()),
]
