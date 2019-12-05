from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='mfapp-home'),
    path('about/',views.about,name='mfapp-about'),
]
