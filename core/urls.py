from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:short_url>', views.redirect_url_cache, name='redirect_url_cache'),
    path('n/<str:short_url>', views.redirect_url, name='redirect_url_normal'),
    path('e/<str:short_url>', views.redirect_url_elastic, name='redirect_url'),
]
