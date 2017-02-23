from django.conf.urls import url
# Controller - route methods
from . import views
urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^register$", views.register, name="register"),
	url(r"^login$", views.login, name="login"),
	url(r"^logout$", views.logout, name="logout"),
	url(r"^success$", views.success, name="success")
    url(r'^create_message$', views.create_message, name="create_message"),
    url(r'^create_comment$', views.create_comment, name="create_comment"),
    url(r'^delete_message$', views.delete_message, name="delete_message"),
]
