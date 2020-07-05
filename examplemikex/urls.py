from django.urls import path, include
from examplemikex import views


urlpatterns = [
    path('', views.index, name='Index')
]