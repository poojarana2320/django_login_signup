from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^signup$', views.signup_view, name='signup'),
    url(r'^login$', views.login_View, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
]
