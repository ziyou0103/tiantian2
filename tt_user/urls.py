from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^login_handle/$', views.login_handle),
    url(r'^register_exists/$', views.register_exists),
    url(r'^info/$', views.info),
    url(r'^order/$', views.order),
    url(r'^site/$', views.site),
    url(r'^site_handle/$', views.site_handle),
]