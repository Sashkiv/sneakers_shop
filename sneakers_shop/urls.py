from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [

    url(r'', include('sneakers_shop.pkg.main.urls')),
    url(r'^sneakers/', include('sneakers_shop.pkg.sneakers.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns("/")
