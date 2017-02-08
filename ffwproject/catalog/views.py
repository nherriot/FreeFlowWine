from django.shortcuts import get_object_or_404, render, render_to_response
from catalog.models import Category, Product
from django.template import RequestContext
from django.urls import reverse



def index(request, template_name="catalog/index.html"):
    page_title = 'Free Flow Wines Catalog Index'
    return render(template_name)

def show_category(request, category_slug, template_name='category.html'):
    print "We are in show_category"
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    context = {'title':page_title,
               'products':products,
               'meta_keywords':meta_keywords,
               'meta_description':meta_description}

    return render(template_name, context)

def show_product(request, product_slug, template_name='Catalog/product.html'):
    print "We are in show_product. product_slug is: {}".format(product_slug)
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description

    context = {'title':page_title,
               'category':categories,
               'meta_keywords':meta_keywords,
               'meta_description': meta_description}

    return render(template_name, context)


def product_page(request):
    context = {'title':'product page'}
    return render(request, 'catalog_index.html', context)

def category_page(request):
    context = {'title':'category page'}
    return render(request, 'catalog_index.html', context)


def dashboard_page2(request):
    context = {}
    #print "A wrong reverse is: ", reverse('news-year-archive')
    #print "dashboard reverse for: {}. is: {}".format('dashboard', reverse('cms:admin_page'))
    return render(request, '../templates/backend/admin_dashboard.html', context)
