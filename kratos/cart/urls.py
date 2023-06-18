from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:id>', views.add, name='add_item'),
    path('remove/<int:id>', views.remove, name="remove_item"),
    path('remove_all', views.remove_all, name="remove_all"),
    path('buy', views.buy, name="buy"),
    path('thanks', views.thanks, name="thanks"),
]
