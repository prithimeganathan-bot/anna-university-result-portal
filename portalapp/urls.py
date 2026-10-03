from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.get_result, name='get_result'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('institution-login/', views.institution_login, name='institution_login'),
    path('inst-dashboard/', views.inst_dashboard, name='inst_dashboard'),
    path('inst-logout/', views.inst_logout, name='inst_logout'),
    path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
]