from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # ✅ Redirect import karo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('register/')),  # ✅ Default URL ko register page pe redirect karo
    path('', include('users.urls')),
]
