from django.urls import path
from .views import HomeView, ItemDetailView
from . import views

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
