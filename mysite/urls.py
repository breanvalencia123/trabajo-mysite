from django.contrib import admin
from django.urls import path
from catalog import views as catalog_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',catalog_views.index, name='index')
	]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)