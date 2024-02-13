from django.shortcuts import render

# Create your views here.

def home(request):
    current_page = 'home'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/home.html', context)