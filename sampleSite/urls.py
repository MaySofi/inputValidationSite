from django.urls import path
from simpleSite import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.handle_submission, name='submit'),
]