from django.db import models
from django.utils import timezone

import datetime


class Poll(models.Model):
    question = models.CharField(max_length=140)
    pub_date = models.DateTimeField('Tiempo de Publicacion')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently'

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text
