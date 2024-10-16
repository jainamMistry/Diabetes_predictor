from django.urls import path
from . import views

# Namespacing the app URLs with the app name
app_name = 'diabetes_predictor'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('prediction/', views.prediction, name='prediction'),
    path('result/', views.result, name='result'),
    path('about_us/', views.about_us, name='about_us')
]