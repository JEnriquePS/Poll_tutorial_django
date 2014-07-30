from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from models import Poll, Choice
import datetime


def tiempo_actual(request):
    ahora = datetime.datetime.now()
    html = "<html><body>esta es mi hora %s </body></html>" % ahora
    return HttpResponse(html)


def incrementar_tiempo(request, aumento):
    aumento = int(aumento)
    dt = datetime.datetime.now() + datetime.timedelta(hours=aumento)
    html = "<html><body>esta es mi hora %s </body></html>" % dt
    return HttpResponse(html)

def poll_vista(request):
    pregunta = Poll.objects.all().order_by('-pub_date')
    context = {'poll_lista_pregunta':pregunta}
    return render(request,'home.html', context)

def detalle_poll(request, pk):
    pre = get_object_or_404(Poll, pk=pk)
    return render(request, 'detail.html', {'pregunta':pre})
