from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('account/', include('account.urls'), name='account'),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    # tailwind urls
    path("__reload__/", include("django_browser_reload.urls")),
]
