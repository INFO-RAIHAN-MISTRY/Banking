from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.auth_login, name='Login'),
    path('user/dashboard/', views.dashboard, name='Dashboard'),
    path('user/customers/', views.all_customers, name='Customers'),
    path('user/view/customers/<slug>/', views.view_customer, name='View_customers'),
    path('user/update/customers/<slug>/', views.update_customer, name='Update_customers'),
    path('user/delete/customers/<slug>/', views.delete_customer, name='Delete_customers'),
    path('user/add/customer', views.add_customer, name='Add_customer'),
    path("user/banks&cards/",views.Banks_Cards, name="Banks_Cards"),
    path('user/dashboard/logout/', views.auth_logout, name='Logout'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
