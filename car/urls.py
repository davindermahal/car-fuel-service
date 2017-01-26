from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add/$', views.add, name='car_add'),
    url(r'^edit/(?P<car_id>\d+)/$', views.edit, name='car_edit'),
    url(r'^(?P<car_id>\d+)/$', views.detail, name='car_detail'),
    url(r'^$', views.index, name='car_index'),
]
