from django.conf.urls import patterns
from views import tiempo_actual

urlpatterns = patterns('poll.views',
                       (r'^time/$', tiempo_actual),
)
