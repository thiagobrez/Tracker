from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clock import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name='index'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, name='logout'),
]