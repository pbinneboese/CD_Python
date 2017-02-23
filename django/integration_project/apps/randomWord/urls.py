from django.conf.urls import url
# Controller - route methods
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create")
]
