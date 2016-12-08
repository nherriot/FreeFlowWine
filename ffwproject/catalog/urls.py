from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from catalog.views import category_page, product_page, show_category, show_product


urlpatterns = [
    url(r'^product/(?P<product_slug>[-\w]+)/$', show_product, name="product"),
  	url('^category/(?P<category_slug>[-\w]+)/$', show_category, name='category'),

]
