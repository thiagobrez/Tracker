from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clock import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin/', admin.site.urls),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^home', views.home, name='home'),
	url(r'^timer', views.timer, name='timer'),
	url(r'^profile/(?P<username>[\w.@+-]+)/$', views.profile, name='profile'),

]
