from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('booking/', views.register, name='register'),
    path('register/', views.register_client, name='register_client'),
    path('success/', views.success_view, name='success_view'),
    path('terms/', views.terms_view, name='terms_view'), 
    path('privacy/', views.privacy_view, name='privacy_view'),
    path('partner/', views.partnership_view, name='partner_view'),
    path('google54831a9074c5fe25.html', TemplateView.as_view(template_name='google54831a9074c5fe25.html')),
]