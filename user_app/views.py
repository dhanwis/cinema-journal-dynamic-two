from django.shortcuts import render
from admin_app.models import LatestRelease

# Create your views here.

def home(request):
    current_page = 'home'
    latest_releases_one = LatestRelease.objects.all().order_by('-id')[0:4]
    latest_releases_two = LatestRelease.objects.all().order_by('-id')[4:8]

    

    context = {
        'current_page': current_page,
        'latest_releases_one' : latest_releases_one,
        'latest_releases_two' : latest_releases_two
    }
    return render(request, 'user_app/pages/home.html', context)

def latest_release(request):
    current_page = 'latest_release'
    latest_releases = LatestRelease.objects.all()
    context = {
        'current_page': current_page,
        'latest_releases' : latest_releases
    }
    return render(request, 'user_app/pages/latest_release.html', context)

def location_report(request):
    current_page = 'location_report'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/location_report.html', context)

def meet_the_person(request):
    current_page = 'meet_the_person'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/meet_the_person.html', context)

def teaser_and_promose(request):
    current_page = 'teaser_and_promose'
    context = {
        'current_page': current_page,
    }
    return render(request, 'user_app/pages/teaser_and_promose.html', context)