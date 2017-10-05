from  django.conf.urls import url


from .views import (
    home,
    post_create,
    post_detail,
)

urlpatterns = [
    url(r'^$',home,name='home'),
    url(r'^create/$',post_create,name='home'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]






