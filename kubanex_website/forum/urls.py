from django.urls import path
from .views import index, sign_up

app_name = 'forum'
urlpatterns = [
    path('', index, name='homepage'),
    path('register/', sign_up, name='registration'),
]
