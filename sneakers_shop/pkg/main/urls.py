from django.conf.urls import url
from sneakers_shop.pkg.main.views import IndexView, AboutView, ContactsView, \
    CatalogView, DeliveryView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^about/', AboutView.as_view()),
    url(r'^contacts/', ContactsView.as_view()),
    url(r'^catalog/', CatalogView.as_view()),
    url(r'^delivery/', DeliveryView.as_view()),
]
