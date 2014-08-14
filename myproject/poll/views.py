from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    pregunta = Poll.objects.all().order_by('-id')[:6]
    context = {'poll_lista_pregunta':pregunta}
    return render(request, 'home.html', context)


def detalle_poll(request, pk):
    pre = get_object_or_404(Poll, pk=pk)
    return render(request, 'detail.html', {'pregunta':pre})


def detalle_choice(request, choice_id):
<<<<<<< HEAD
    choice_text = get_object_or_404(Choice, pk = choice_id)
    return render(request, 'choice_detalle.html', {'choice_id':choice_text})


=======
    choice_text = get_object_or_404(Choice, pk=choice_id)
    return render(request, 'choice_detalle.html', {'choice_id': choice_text})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selectd_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'poll': p, 'error_message': "seleccion no valida"})
    else:
        selectd_choice.votos = True
        selectd_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

>>>>>>> e5b2f5255e0e4e2ef1d8213869ca09614776cd4f
