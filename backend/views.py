from django.http import JsonResponse
from .models import *
from django.db.models import Count
from grappelli_extras.utils import Codec


def dashboard(request):
    marcas = []
    for m in Brand.objects.all():
        marcas.append({'label': m.name,
                       'y': Active.objects.filter(brand=m).count()})
    estados = []
    for m in Status.objects.all():
        estados.append({'label': m.name,
                       'y': Active.objects.filter(status=m).count()})
    areas = []
    for m in Area.objects.all():
        areas.append({'label': m.name,
                       'y': Active.objects.filter(area=m).count()})

    return JsonResponse({'marcas': marcas, 'estados': estados, 'areas': areas}, encoder=Codec)
