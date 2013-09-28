from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from app.views import sms

# Uncomment the next two lines to enable the admin:
import djadmin2

djadmin2.default.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'sms', sms),
    # Examples:
    # url(r'^$', 'outpatient.views.home', name='home'),
    # url(r'^outpatient/', include('outpatient.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin2/', include(djadmin2.default.urls)),
    # url(r'^admin/', include(admin.site.urls)),
)
