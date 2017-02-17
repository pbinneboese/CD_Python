from django.conf.urls import url
# Controller - route methods
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^users$', views.show),
    url(r'^new_user$', views.create)
]
