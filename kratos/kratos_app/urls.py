from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('components/<int:id>/', views.component_details, name="component_details"),
    path('profile/', views.profile, name="profile"),
    path('favorites/', include('favorites.urls')),
    path('cart/', include('cart.urls')),
]

