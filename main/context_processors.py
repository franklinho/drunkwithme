from django.conf import settings

def domain_url(request):
    return {'DOMAIN_URL':settings.DOMAIN_URL}
