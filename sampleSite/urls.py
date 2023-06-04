from django.urls import path

from simpleSite import views
from myApp import views as v
urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.handle_submission, name='submit'),
    path('app', v.start, name='app')
]
