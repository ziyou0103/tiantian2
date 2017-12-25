from django.conf.urls import url
from tt_cart import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add_(\d+)_(\d+)/$', views.add),
    url(r'^edit(\d+)_(\d+)/$', views.edit),
    url(r'^delete(\d+)/$', views.delete),
]