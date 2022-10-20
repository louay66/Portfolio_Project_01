"""Portfolio_Project_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from pages import views

from django.conf.urls.static import static

import pages

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('pages.urls')),

    path('rest/bookings/', views.Booking_list.as_view()),
    path('rest/bookings/<int:pk>', views.Booking_delete_update.as_view()),
    path('rest/products/', views.Product_list.as_view()),
    path('rest/products/<int:pk>', views.Product_delete_update.as_view()),
    path('rest/category/', views.Category_list.as_view()),
    path('rest/category/<int:pk>', views.Category_delete_update.as_view()),
    path('rest/guests/', views.Guest_list.as_view()),
    path('rest/guests/<int:pk>', views.Guest_delete_update.as_view()),
    path('api-auth', include('rest_framework.urls')),
    # path('api-token-auth', obtain_auth_token),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
