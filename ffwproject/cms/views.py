from django.shortcuts import render

# Create your views here.


def index_page(request):
    context = {}
    return render(request, 'index.html', context)


def dashboard_page(request):
    context = {}
    return render(request, '../templates/backend/admin_dashboard.html', context)
