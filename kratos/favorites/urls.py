from django.urls import path
from favorites import views

urlpatterns = [
    path('favorites/', views.favorites, name='favorites'),
    path('add/<int:id>', views.add, name='add_favorites'),
    path('remove/<int:id>', views.remove, name="remove_favorites"),
]
