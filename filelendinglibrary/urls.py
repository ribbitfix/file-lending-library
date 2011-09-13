from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^lendinglib/$', 'lendinglibapp.views.index'),
    url(r'^lendinglib/my_profile/(?P<user_id>\d+)/$', 'lendinglibapp.views.my_profile'),
    url(r'^lendinglib/friend_profile/(?P<user_id>\d+)/$', 'lendinglibapp.views.friend_profile'),
    url(r'^lendinglib/basic_profile/$', 'lendinglibapp.views.basic_profile'),
    url(r'^lendinglib/file_detail/(?P<file_id>\d+)/$', 'lendinglibapp.views.file_detail'),
    # Examples:
    # url(r'^$', 'filelendinglibrary.views.home', name='home'),
    # url(r'^filelendinglibrary/', include('filelendinglibrary.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
