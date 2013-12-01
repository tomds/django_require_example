from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^e1/$', TemplateView.as_view(template_name='e1.html')),
)
