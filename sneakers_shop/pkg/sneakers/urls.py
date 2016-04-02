from django.conf.urls import url

from sneakers_shop.pkg.sneakers.views import SneakersCatalogView, \
    SneakersDetailView, SneakersListView, PromoListView, OrderView

urlpatterns = [
    url(r'^promo_list/', PromoListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/order/$', OrderView.as_view()),
    url(r'^(?P<pk>[0-9]+)/', SneakersDetailView.as_view()),
    url(r'^list/', SneakersListView.as_view()),
    url(r'^$', SneakersCatalogView.as_view()),
]
