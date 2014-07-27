from django.db import models


class Poll(models.Model):
    pregunta = models.CharField(max_length=140)
    pub_date = models.DateTimeField('Tiempo de Publicacion')

    def __unicode__(self):
        return self.pregunta


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    opcion = models.CharField(max_length=50)
    votos = models.IntegerField()

    def __unicode__(self):
        return self.opcion