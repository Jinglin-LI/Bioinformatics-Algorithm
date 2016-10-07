from django.conf.urls import url,include
from . import views


urlpatterns = [
	#exercise/
	url(r'^$', views.index, name = 'exerciseIndex'),
]