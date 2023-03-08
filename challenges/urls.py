from django.urls import path
from . import views


urlpatterns = [
    #path('january/', views.index ),
    #path('february/', views.feb ),
    path("<month>", views.monthly_challenge),
]