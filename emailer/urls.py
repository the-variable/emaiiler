from django.urls import path
from .views import *

urlpatterns = [
    path('', send),
    path('csrf-token/', csrf_token_view),
]