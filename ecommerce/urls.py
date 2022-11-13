from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# TODO: Remover debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    # TODO: Remover debug toolbar
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
