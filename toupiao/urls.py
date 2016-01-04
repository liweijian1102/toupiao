from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'toupiao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',views.login),
    url(r'^acc_login/',views.acc_login),
    url(r'^vote/',views.vote),
    url(r'^vote_content_single',views.vote_content_single),
    url(r'^vote_single_add/',views.vote_single_add),
    url(r'^vote_content_double',views.vote_content_double),
    url(r'^vote_content_tex',views.vote_content_tex),
    url(r'^vote_tab_add',views.vote_tab_add),
    url(r'^vote_tab',views.vote_tab),
    url(r'^vote_create',views.vote_create),
)
