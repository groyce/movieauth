from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from api import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('', views.movie_list),
    url(r'^api/movies/$', views.movie_list),
    url(r'^api/movies/(?P<pk>[0-9]+)$', views.getMovie),
    path('auth/', include('auth.urls')),
]