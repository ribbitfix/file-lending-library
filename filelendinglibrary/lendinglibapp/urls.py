from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('lendinglibapp.views',
    url(r'^$', 'index'),
    url(r'^my_profile/(?P<user_id>\d+)/$', 'my_profile', name='my_profile'),
    url(r'^friend_profile/(?P<user_id>\d+)/$', 'friend_profile'),
    url(r'^basic_profile/$', 'basic_profile'),
    url(r'^file_detail/(?P<file_id>\d+)/$', 'file_detail'),
)
    # Examples:
    # url(r'^$', 'filelendinglibrary.views.home', name='home'),
    # url(r'^filelendinglibrary/', include('filelendinglibrary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
