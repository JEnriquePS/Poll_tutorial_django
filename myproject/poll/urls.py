from django.conf.urls import patterns, url


urlpatterns = patterns('poll.views',
                       url(r'^time/$', 'tiempo_actual', name='detail1'),
                       url(r'^add_time/(\d{1,2})/$', 'incrementar_tiempo',
                        name='detail2'),
                       url(r'^poll/$', 'poll_vista',name='detail2'),
                       url(r'^(?P<pk>\d+)/$', 'detalle_poll',
                        name='detalle_poll'),
)
