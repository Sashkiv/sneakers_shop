from django.conf.urls import url

from sneakers_shop.pkg.sneakers.views import SneakersListView, \
    SneakersDetailView

urlpatterns = [
    url(r'^sneakers/(?P<pk>[0-9]+)/', SneakersDetailView.as_view()),
    url(r'^sneakers/', SneakersListView.as_view()),
]
