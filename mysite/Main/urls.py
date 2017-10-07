from  django.conf.urls import url


from .views import (
    home,
    post_create,
    post_detail,
    our_team,
    add_member,
    dash_board,
    post_list,
    post_update,
    post_delete,
    property_listing,
    single_members_details,
    gallery,
    dash_board_help,
)

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^create/$',post_create,name='home'),
    url(r'^$',post_list,name='list'),
    url(r'^dashboard/$', dash_board,name='dashboard'),
    url(r'^dashboard-help/$',dash_board_help,name='dash_help'),
    url(r'^property-listing/$',property_listing,name='listing'),
    url(r'^add-member/$',add_member,name='add-member'),
    url(r'^(?P<id>\d+)$',single_members_details,name='single_member_detail'), 
    url(r'^gallery/$',gallery,name='gallery'),   
    url(r'^our-team/$',our_team,name='our_team'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]

