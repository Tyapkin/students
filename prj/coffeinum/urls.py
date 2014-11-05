from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views import IndexView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounting-students/', include('students.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
