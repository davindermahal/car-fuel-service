from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^car/(?P<car_id>\d+)/$', views.upload_file, name='importer_add'),
]
