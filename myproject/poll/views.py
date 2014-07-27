from django.shortcuts import render
from django.http import HttpResponse
import datetime


def tiempo_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body>esta es mi hora %s </body></html>" % ahora
    return HttpResponse(html)

