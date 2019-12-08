from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('crm.urls')),
    path('account/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)