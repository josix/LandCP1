from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^$', views.home_page),
        url(r'login/', views.my_login, name ="login"),
        url(r'signup/', views.sign_up_page, name ="signup_page"),
        url(r'signup_result/', views.sign_up, name ="signup_result")
]
