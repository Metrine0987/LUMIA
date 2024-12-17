from django.urls import path
from .import views

app_name ='myapp'
     
urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('contact/', views.contact_page, name ='contact' ),
    path('about/', views.about_page, name='about'),
    path('portfolio/', views.portfolio_page, name = 'portfolio'),
    path('service/', views.service_page, name ='service'),
    path('starter/', views.starter_page, name = 'starter'),
    path('team/', views.team_page, name = 'team'),
    
]