from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('kviz/', include('kviz.urls')),
    path('admin/', admin.site.urls),
]