from django.urls import path

from surur.views import Home, AboutUs

urlpatterns = [
    path('', Home.as_view()),
    path('about-us/', AboutUs.as_view()),
    path('reservation/', AboutUs.as_view()),
]
