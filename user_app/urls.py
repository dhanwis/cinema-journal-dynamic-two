from django.urls import path
from user_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('latest/release', latest_release, name='latest_release'),
    path('location/report', location_report, name='location_report'),
    path('meet/the/person', meet_the_person, name='meet_the_person'),
    path('teaser/and/promose', teaser_and_promose, name='teaser_and_promose'),
]