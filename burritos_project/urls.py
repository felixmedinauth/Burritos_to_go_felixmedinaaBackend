"""
URL configuration for burritos_project project.
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
# Importar la vista necesaria para el login por token
from rest_framework.authtoken.views import obtain_auth_token 


def redirect_to_api(request):
    """Redirige la raíz del sitio a la URL de la API."""
    return redirect('api/')


urlpatterns = [
    # 1. Redirección de la raíz del sitio
    path('', redirect_to_api, name='redirect-to-api'),

    # 2. Panel de administración
    path('admin/', admin.site.urls),

    # 3. Inclusión de las URLs de la aplicación 'core' (Tus endpoints principales)
    path('api/', include('core.urls')),

    # 4. RUTA DE LOGIN DE API (AUTENTICACIÓN POR TOKEN)
    # Los clientes enviarán un POST con 'username' y 'password' a esta ruta
    # y recibirán un token si las credenciales son válidas.
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
]