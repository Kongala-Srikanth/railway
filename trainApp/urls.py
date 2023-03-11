from django.urls import path
from trainApp.views import *

urlpatterns = [
    path('register/',register),
    path('search/',searching),
    path('booking/',booking),
]
