from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def index_page(request):
    context = {}
    return render(request, 'index.html', context)


def dashboard_page(request):
    context = {}
    #print "A wrong reverse is: ", reverse('news-year-archive')
    #print "dashboard reverse for: {}. is: {}".format('dashboard', reverse('cms:admin_page'))
    return render(request, '../templates/backend/admin_dashboard.html', context)
