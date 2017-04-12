from django.conf.urls import url, include
from . import views

urlpatterns = [
        url(r'^', views.produce_three_number, name ="roll_call"),
]
