from  django.conf.urls import url


from .views import (
    post_create,
    about,
    gallery,
    sell_form,
    get_back,
    post_list,
    post_detail,
    dash_board,
    dash_board_help,
    property_listing,
    add_member,
    single_members_details

   
)

urlpatterns = [
    url(r'^$',property_listing,name='home'),
    url(r'^about-us/$', about,name='about'),
    url(r'^gallery/$', gallery,name='gallery'),
    url(r'^dashboard/$', dash_board,name='dashboard'),
    url(r'^dashboard-help/$',dash_board_help,name='dash_help'),
    url(r'^add-member/$',add_member,name='add-member'),
    url(r'^(?P<id>\d+)$',single_members_details,name='single_member_detail'), 
    url(r'^create/$',post_create,name='create'),
    url(r'^sell-to-us/$',sell_form,name='sell_form'),
    url(r'^get-back-to-you/$',get_back,name='get_back'),
    url(r'^property-listing/$',post_list,name='listing'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]
