from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^car/(?P<car_id>\d+)/add/$', views.add_for_car, name='fuel_add_for_car'),
    url(r'^car/(?P<car_id>\d+)/view/$', views.view_for_car, name='fuel_view_for_car'),
    url(r'^car/(?P<car_id>\d+)/edit/(?P<fill_up_id>\d+)$', views.edit, name='fuel_edit'),
    url(r'^car/(?P<car_id>\d+)/(?P<fill_up_id>\d+)/$', views.detail, name='fuel_detail'),
]
