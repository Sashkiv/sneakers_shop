from django.conf.urls import url
from sneakers_shop.pkg.main.views import IndexView, AboutView, ContactsView, \
    CatalogView, DeliveryView, GoogleVerification

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^about/', AboutView.as_view()),
    url(r'^contacts/', ContactsView.as_view()),
    url(r'^catalog/', CatalogView.as_view()),
    url(r'^delivery/', DeliveryView.as_view()),
    url(r'^google4346c5c573bda2ea\.html', GoogleVerification.as_view()),
]
