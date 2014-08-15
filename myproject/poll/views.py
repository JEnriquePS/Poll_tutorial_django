from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect  # ,Http404
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


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:6]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'home.html', context)


# def detail(request, poll_id):
#     "importar Http404"
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#     return render(request, 'detail.html', {'poll': poll})


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'detail.html', {'poll': poll})


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'results.html', {'poll': poll})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selectd_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'poll': p,
                      'error_message': "seleccion no valida"})
    else:
        selectd_choice.votes += 1
        selectd_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
