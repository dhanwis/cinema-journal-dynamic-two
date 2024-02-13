from django.shortcuts import render

# Create your views here.

def dashboard(request):
    current_page = 'dashboard'
    context = {
        'current_page': current_page,
    }
    return render(request, 'admin_app/pages/dashboard.html', context)