from django.conf.urls import url
from django.contrib import admin
from .import views
app_name='user'
urlpatterns = [
			#re_path(r'^profile/(?P<username>[\w.@+-]+)/$', profile_detail, name='profile'),
			#url(r'^query/$', views.testing),  [/w.@+-]+)/$
			#url(r'^upload$', views.newdesign, name='newdesign'),
			url(r'^(?P<username>[a-zA-Z0-9]+)/$', views.get_user_profile),
			url(r'^update/(?P<username>[a-zA-Z0-9]+)/$', views.edit_user, name='account_update'),
			#url(r'^update/(?P<username>[a-zA-Z0-9]+)/$', views.edit_user, name='account_update'),
			#url(r'^upload$', views.newdesign, name='newdesign'),	
]