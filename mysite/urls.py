from django.conf.urls import url, include
from mysite import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^$', views.home, name='homePage'),
    url(r'^beta/$', views.beta, name='beta'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^homelogin/$', views.Homelogin, name='loginHandler'),
    url(r'^store/$', views.store, name='store'),
    url(r'^log/$', views.log_data, name='log_data'),
    url(r'^latest/$', views.latest_entry, name='latest'),
]
