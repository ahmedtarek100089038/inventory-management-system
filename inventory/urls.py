from django.contrib import admin
from django.urls import path, include
# from inventoryapi.views import InventoryList
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventoryapi.urls')),
    
]
