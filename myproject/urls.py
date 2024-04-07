from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include your app's URLs
    path('', include('professional.urls')),  # Include your app's URLs
    path('', include('blog.urls')),  # Include your app's URLs

]
