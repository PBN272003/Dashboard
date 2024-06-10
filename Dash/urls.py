from .models import User 
from django.urls import path
from .views import dash_data,dashView,dashboard

urlpatterns = [
   # path('upload-json/',import_data,name='upload-json'),
   path('upload-data/',dash_data,name = 'upload-data'),
   path('data/',dashView.as_view(), name='data'),
   path('',dashboard,name = 'dashboard'),
]