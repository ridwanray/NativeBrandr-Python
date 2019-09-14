from django.conf.urls import url
from django.contrib import admin
from .import views
app_name='category'
urlpatterns = [	
			url(r'^cap/$', views.cap, name='catcap'),
			url(r'^trousers&shirts/$', views.trousersshirts,  name='catsshirt'),		
			url(r'^customized-vest/$', views.customizedvest,  name='catcusvest'),	
			url(r'^bags&add-ons$', views.bagsaddons,  name='catbag'),	
			url(r'^jewelry$', views.jewelry,  name='cajewel'),	
			url(r'^native-wears/$', views.nativewears,  name='catantice'),	
			url(r'^shirts/$', views.shirts,  name='catshirt'),	
			url(r'^footwears/$', views.footwears,  name='catfootwear'),	
			#url(r'^(?P<category>[a-zA-Z0-9]+)/$', views.categorypage),	
			#url(r'^(?P<category>[a-zA-Z0-9]+)/$', views.categorypage),	
			#url(r'^(?P<category>[a-zA-Z0-9]+)/$', views.categorypage),	
			#url(r'^(?P<>[a-zA-Z0-9]+)/$', views.get_user_profile),
			#url(r'^(?P<>[a-zA-Z0-9]+)/$', views.get_user_profile),
]
