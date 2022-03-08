from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cart-item/', CartItemViews.as_view()),
    path('cart-item/<int:id>/', CartItemViews.as_view())
]
