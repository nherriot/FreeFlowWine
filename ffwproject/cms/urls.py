from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from cms.views import index_view, dashboard_view


urlpatterns = [
    url('^$', index_view, name='index'),
    url('^dashboard/$', dashboard_view, name='admin_page'),
]
