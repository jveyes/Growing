from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppGrowing.urls')),  # Ensure this line includes the empty path
]