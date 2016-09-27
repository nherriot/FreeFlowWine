from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from cms.views import index_page


urlpatterns = [
	url('^$', index_page, name='index'),
]