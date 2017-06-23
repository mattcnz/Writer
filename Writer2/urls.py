"""Writer2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from books import views
from django.conf.urls.static import static
import Writer2.settings as settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login',
        kwargs={'redirect_authenticated_user': True}),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^book_viewer/([0-9]+)/$', views.book_viewer, name='book_viewer'),
    
    url(r'^new_book_bs/$', views.new_book_bs, name='new_book_bs'),
    url(r'^save_ajax/([0-9]+)/$', views.save_ajax, name='save_ajax'),
    url(r'^out_of_time/([0-9]+)/$', views.out_of_time, name='out_of_time'),
    url(r'^directory/$', views.directory, name='directory'),
    url(r'^info/$', views.display_some_info, name='info'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.directory, name='directory'),
    
]

urlpatterns += staticfiles_urlpatterns()
