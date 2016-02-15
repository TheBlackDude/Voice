from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('', 
     url(r'^contact/$', views.contact, name='contact'),
     url(r'^faq/$', views.question, name='faq'),
     url(r'^education/$', views.education, name='education'),
     url(r'^dawa/$', views.dawa, name='dawa'),
     url(r'^research/$', views.research, name='research'), 
)
