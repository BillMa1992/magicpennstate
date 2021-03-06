from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views



from trademap import views
from trademap.views import *


urlpatterns = [
        url(r'^login/$', auth_views.login),
		url(r'^register/$', register),
		url(r'^register/success/$', register_success),
		url(r'^logout/$', logout_page),
]
