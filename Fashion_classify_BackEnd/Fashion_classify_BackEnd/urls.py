"""Fashion_classify_BackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
# from rest_framework.routers import SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from uploadapp import views

# router = SimpleRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base-api/upload_images/', views.FileUploadView.as_view(), name='Upload_fashion_images'),
    path('base-api/get_uploaded_images/', views.ImagesView.as_view(), name='Get_Upload_fashion_images'),
    path('base-api/save_clothings/', views.ClothingsView.as_view(), name='save_clothing'),
    path('base-api/save_predictions/', views.PredictionsView.as_view(), name='Save_predictions_and_updates'),
    path('base-api/get_uploaded_clothing_images/', views.ClothingImagesView.as_view(), name='Get_Clothing_fash_images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
