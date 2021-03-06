from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
path('become_vendor/', views.become_vendor, name = 'become_vendor'),
path('vendor_admin/', views.vendor_admin, name='vendor_admin'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

]
