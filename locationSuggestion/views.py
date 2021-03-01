from rest_framework.views import APIView
from django.http import JsonResponse
import requests
from suggestion.settings import weather_api_key,geo_api_key
# Create your views here.
geocode_headers = {"apikey": geo_api_key}
geo_api_url = "https://app.geocodeapi.io/api/v1/search"
weather_api_url = "http://api.openweathermap.org/data/2.5/weather?q="

"""
geoSUggestion:Api for get details of City as per city name
"""
class CitySuggestion(APIView):
    def get(self,request):
        try:
            city_name = request.GET.get("cityName","")
            if city_name == "":
                response = {
                    "message":"CityName feild is required and should Not be blank"
                }
                return JsonResponse(response,status=411)
            params = (
                ("text", city_name),
            )
            response = requests.get(geo_api_url, headers=geocode_headers, params=params)
            if response.status_code == 200:
                response = {
                    "message": "city Found successfull",
                    "responseData":response.json()
                }
                return JsonResponse(response, status=200)
            else:
                response = {
                    "message": "City Not found"
                }
                return JsonResponse(response, status=404)
        except:
            response = {
                "message": "Internal Server Error"
            }
            return JsonResponse(response, status=500)

"""
WeatherDetails:Api for get details of weather as per city name and id
"""
class WeatherDetails(APIView):
    """
    cityName:get city name in rquest param
    """
    def get(self,request):
        try:
            city_name = request.GET.get("cityName","")
            if city_name == "":
                response = {
                    "message":"CityName feild is required and should Not be blank"
                }
                return JsonResponse(response,status=411)
            url = weather_api_url+city_name+"&appid="+weather_api_key
            response = requests.get(url)
            if response.status_code == 200:
                response = {
                    "message": "Weather data found successfully",
                    "responseData": response.json()
                }
                return JsonResponse(response, status=200)
            else:
                response = {
                    "message": "Weather not found"
                }
                return JsonResponse(response, status=404)
        except:
            response = {
                "message": "Internal Server Error"
            }
            return JsonResponse(response, status=500)

