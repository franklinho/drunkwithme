from django.conf import settings

def googlemaps_api_key(request):
    return {"GOOGLEMAPS_APIKEY":settings.GOOGLEMAPS_APIKEY}
