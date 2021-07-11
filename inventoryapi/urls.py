from django.urls import path
from .views import InventoryView


urlpatterns = [
    path('inventory/<int:pk>', InventoryView.as_view()),
    path('inventory/', InventoryView.as_view()),
]
