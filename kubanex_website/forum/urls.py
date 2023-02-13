from django.urls import path
from .views import index, sign_up

urlpatterns = [
    path('', index, name='homepage'),
    path('register/', sign_up, name='registration'),
]
