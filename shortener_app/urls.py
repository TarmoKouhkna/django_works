from django.urls import path
from .views import AliasCreateView, redirect_view, clear_aliases

urlpatterns = [
    path('', AliasCreateView.as_view(), name='create'),
    path('clear/', clear_aliases, name='clear_aliases'),
    path('<str:alias>/', redirect_view, name='redirect'),
]
