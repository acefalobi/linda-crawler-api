from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('crawler.urls', 'crawler'), namespace='crawler')),
    path('admin/', admin.site.urls),
]
