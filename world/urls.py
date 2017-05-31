from django.conf.urls import url

from . import views

app_name = 'world'
urlpatterns = [
    url(r'^', views.map_view, name='map'),
]