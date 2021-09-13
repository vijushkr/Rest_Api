from django.conf.urls import url
from hospitalweb import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  url(r'^api/patient$', views.users_list),
  url(r'^api/patient/(?P<pk>[0-9]+)$', csrf_exempt(views.user_detail)),
  url(r'^api/patient/(?P<pk>[0-9]+)$', csrf_exempt(views.user_delete)),
  ]