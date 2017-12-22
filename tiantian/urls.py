from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('tt_user.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('tt_goods.urls')),
]
