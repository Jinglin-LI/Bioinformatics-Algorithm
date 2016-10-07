"""lsm2241 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from lsm2241.view import home
from lsm2241.view import contactus
from lsm2241.view import coursecontents
from lsm2241.view import exercise


urlpatterns = [
	url(r'^$', home, name = 'home'),
	url(r'^home', home, name = 'home'),
	url(r'^contactus', contactus, name = 'contactus'),
	url(r'^coursecontents', coursecontents, name = 'coursecontents'),
    url(r'^exercise/', include('exercise.urls')),
    #url(r'^exerciseIndex', exercise, name = 'exerciseIndex'),
]