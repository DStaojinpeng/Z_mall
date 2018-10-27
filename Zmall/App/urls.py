from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login.html$', views.login, name='login'),
    url(r'^register.html$',views.register, name='register'),
]