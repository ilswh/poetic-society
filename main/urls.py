from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include('poems.urls')),
    path("contact/", include('contact.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
