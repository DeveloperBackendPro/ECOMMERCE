from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from home import views
from creatoradmin import views as Creatoradmin

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectlanguage_admin', Creatoradmin.selectlanguage_admin, name='selectlanguage_admin'),
    path('selectlanguage_client', Creatoradmin.selectlanguage_client, name='selectlanguage_client'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns (
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('creatoradmin/', include('creatoradmin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False,
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)