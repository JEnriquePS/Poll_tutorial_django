from django.conf.urls import patterns, url


urlpatterns = patterns('poll.views',
    url(r'^time/$', 'tiempo_actual', name='detail1'),
    url(r'^add_time/(\d{1,2})/$', 'incrementar_tiempo', name='detail2'),
    url(r'^poll/$', 'index', name='index'),
    url(r'^poll/(?P<poll_id>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results', name='results'),
)
