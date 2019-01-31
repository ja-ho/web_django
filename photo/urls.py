from django.conf.urls import url
from photo.views import *


app_name = 'photo'
urlpatterns = [

    # Example: /
    url(r'^$', AlbumLV.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),

    # Example: /album/99
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

    # Example: /photo/99
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),

    # Example: /album/add
    url(r'^album/add/$', AlbumPhotoCV.as_view(), name='album_add'),

    # Example: /album/change
    url(r'^album/change/$', AlbumChangeLV.as_view(), name='album_change'),

    # Example: /album/99/update
    url(r'^album/(?P<pk>\d+)/update/$', AlbumPhotoUV.as_view(),
        name='album_update'),

    # Example: /album/99/delete
    url(r'^album/(?P<pk>\d+)/delete/$', AlbumDeleteView.as_view(),
        name='album_delete'),

    # Example: /photo/add
    url(r'^photo/add/$', PhotoCreateView.as_view(), name='photo_add'),

    # Example: /photo/change
    url(r'^photo/change/$', PhotoChangeLV.as_view(), name='photo_change'),

    # Example: /photo/99/update
    url(r'^photo/(?P<pk>\d+)/update$', PhotoUpdateView.as_view(),
        name='album_update'),

    # Example: /photo/99/delete
    url(r'^photo/(?P<pk>\d+)/delete$', PhotoDeleteView.as_view(),
        name='photo_delete'),
]
