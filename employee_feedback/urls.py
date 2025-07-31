from django.http import JsonResponse
from django.urls import path,include


urlpatterns = [
    path('api/', include('feedback.urls')),
]

