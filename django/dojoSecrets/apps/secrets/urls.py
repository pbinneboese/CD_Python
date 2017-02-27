from django.conf.urls import url
# Controller - route methods
from . import views
urlpatterns = [
	url(r"^success$", views.success, name="success"),
	url(r"^popular$", views.popular, name="popular"),
    url(r"^create_message$", views.create_message, name="create_message"),
    url(r"^create_like/(?P<message_id>\d+)$", views.create_like, name="create_like"),
    url(r"^delete_message/(?P<message_id>\d+)$", views.delete_message, name="delete_message"),
]
