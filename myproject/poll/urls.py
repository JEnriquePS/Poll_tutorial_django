from django.conf.urls import patterns


urlpatterns = patterns('poll.views',
                       (r'^time/$', 'tiempo_actual'),
                       (r'^add_time/(\d{1,2})/$', 'incrementar_tiempo'),
)
