"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV
#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
	#url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),

    # auth url
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

	url(r'^admin/', admin.site.urls),
    #path('admin/', admin.site.urls),
	url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),

	#Class-based views for Bookmark app
	#url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
	#url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
