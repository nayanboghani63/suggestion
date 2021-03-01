from locationSuggestion import views
from django.conf.urls import url

urlpatterns = [
    url(r'^citySuggestion/',views.CitySuggestion.as_view(),name='CitySuggestion'),
    url(r'^weatherDetails/',views.WeatherDetails.as_view(),name='WeatherDetails'),
]