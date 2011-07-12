from django.db import models

class Site(models.Model):
    nome = models.CharField(u'nome', max_length=100)
    template = models.FileField(u'template',upload_to='estrutura/templates')
    def __unicode__(self):
        return u'%s' % (self.nome)

proibidos = ['django.contrib.contenttypes',
    'django.contrib.sessions',
    'portal.estrutura', 
    'django.contrib.admin']

def choices():
    from django.conf import settings
    modulo = ()
    for app in settings.INSTALLED_APPS:
        if not proibidos.__contains__(app): 
            t = ((app.split('.')[-1],app.split('.')[-1]),)
            modulo = modulo.__add__(t)
    return modulo 

class Elemento (models.Model):
    nome = models.CharField(u'nome', max_length=100, choices=choices())
    site = models.ForeignKey('Site')
    template = models.FileField(u'template',upload_to='estrutura/templates')
    def __unicode__(self):
        return u'%s' % (self.nome)

class Instancia(models.Model):
    elemento = models.ForeignKey('Elemento')
    instancia = models.CharField(u'instancia', max_length=100)
    ordem = models.IntegerField(u'ordem')
    def __unicode__(self):
        return u'%s|%s|%s -> %s' % (self.id, self.elemento.nome, self.elemento.site, self.instancia )
