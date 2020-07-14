from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin,auth
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("HelpSystem.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ]