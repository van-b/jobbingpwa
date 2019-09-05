from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from jobado import views
from django.urls import path, include

urlpatterns = [
    path('', include('pwa.urls')),
    path('', views.index, name='index'),
    path('jobado/', include('jobado.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

