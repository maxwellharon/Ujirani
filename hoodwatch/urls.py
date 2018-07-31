from django.conf.urls import url
from . import views
from django.conf.urls.static import static

app_name = 'hoodwatch'

urlpatterns = [
    url(r'^$', views.ListHoodwatchs.as_view(), name='all'),
    url(r'^new/$', views.CreateHoodwatch.as_view(), name='create'),
    url(r'businesses/in/(?P<slug>[-\w]+)/$', views.SingleHoodwatch.as_view(), name='single'),
    url(r'join/(?P<slug>[-\w]+)/$', views.JoinHoodwatch.as_view(), name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$', views.LeaveHoodwatch.as_view(), name='leave'),
]
