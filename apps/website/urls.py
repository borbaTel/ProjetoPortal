from django.urls import path
from apps.website.views import index

urlpatterns = [
    path('', index, name='index'),
]