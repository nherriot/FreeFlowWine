from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from catalog.views import index, category_page, product_page, show_category, show_product


urlpatterns = [
    #url(r'^$', index, {'template_name':'index.html'}, 'catalog_home'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', show_product,{'template_name':'product.html'}, name="product"),
  	url('^category/(?P<category_slug>[-\w]+)/$', show_category, {'template_name':'category.html'}, name='category'),

]
