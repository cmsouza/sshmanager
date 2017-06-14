from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^configFile$', views.config_file, name='config_file'),
]
