from django.conf.urls import url, include
from django.contrib import admin
from . import views
#from signin.regbackend import MyRegistrationView
from django.conf import settings
from django.conf.urls.static import static
app_name='main'

urlpatterns = [
    url( 'adminrilo/', admin.site.urls),
    url(r'^$', views.alldesign, name='all'),
	url(r'^user/', include('user.urls')),
	url(r'^category/', include('category.urls')),
	#url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
	url(r'^dashboard/$', views.dashboard, name='dashboard'),
	url(r'^dashboard/update-profile/(?P<username>[a-zA-Z0-9]+)/$', views.edit_user, name='account_update'),
	#url(r'^newdesign$', views.newdesign, name='newdesign'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 # RegistrationView.as_view(form_class=RegistrationFormTOSAndEmail), 
  #  name='registration_register'