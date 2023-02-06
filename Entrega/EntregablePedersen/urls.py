from django.contrib import admin
from django.urls import path, include
from EntregablePedersen.views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),

    path('Products/', include('Products.urls')),
    path('Categories/', include('Categories.urls')),
    path('Providers/', include('Providers.urls')),
    path('Users/', include('Users.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)