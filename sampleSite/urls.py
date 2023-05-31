from django.urls import path
from simpleSite.views import index

urlpatterns = [
    path('', index),
    path('', index, name='index')
]
