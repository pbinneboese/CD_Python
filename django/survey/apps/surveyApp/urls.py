from django.conf.urls import url
# Controller - route methods
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^result$', views.result),
    url(r'^surveys/process$', views.process)
]
