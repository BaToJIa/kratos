from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from kratos_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kratos_app.urls')),
    path('', include('favorites.urls')),
    path('registration/', views.RegisterView.as_view(), name='register'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name="registration/password-change.html"), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password-change-done.html'), name='password_change_done'),
    path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
