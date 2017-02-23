from django.conf.urls import url
# Controller - route methods
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<color>.*)$', views.ninjas),
]
