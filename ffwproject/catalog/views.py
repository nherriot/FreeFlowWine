from django.shortcuts import render
from django.urls import reverse



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
