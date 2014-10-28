from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'poll.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^poll_demo/', include('poll_demo.urls', namespace="poll_demo")),
    url(r'^admin/', include(admin.site.urls)),
)
