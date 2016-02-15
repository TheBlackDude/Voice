from django.conf.urls import patterns, include, url
from django.contrib import admin
from voice import views

urlpatterns = patterns('', 
     url(r'^$', views.home, name='home'),
     url(r'^voice/', include('voice.urls')), 

     url(r'^admin/', include(admin.site.urls)),
)
