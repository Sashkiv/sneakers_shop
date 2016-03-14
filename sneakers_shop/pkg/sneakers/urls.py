from django.conf.urls import url

from sneakers_shop.pkg.sneakers.views import SneakersListView, \
    SneakersDetailView

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/', SneakersDetailView.as_view()),
    url(r'^$', SneakersListView.as_view()),
]
