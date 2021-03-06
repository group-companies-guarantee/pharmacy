from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('home/', views.home, name='home')
]
