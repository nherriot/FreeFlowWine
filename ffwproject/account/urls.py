from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from account.views import (
			view_profile,
			create_profile,
			update_profile,
			delete_profile,
		)


urlpatterns = [
	
    url('^create/$', views.create_profile, name='create_profile'),
    url('^profile/$', views.view_profile, name='profile'),
    url('^(?P<slug>[\w-]+)/edit/$', views.update_profile, name='update_profile'),
    url('^(?P<slug>[\w-]+)/delete/$', views.delete_profile, name='delete_profile'),
    
]