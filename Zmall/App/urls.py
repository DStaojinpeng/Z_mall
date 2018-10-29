from django.conf.urls import url

from App import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 登录注册
    url(r'^login.html$', views.login, name='login'),
    url(r'^register.html$',views.register, name='register'),

    # 显示产品信息
    # url(r'^product.html\?id=(\d+)$',views.project, name='product')
    url(r'^product.html$',views.project, name='product')

]