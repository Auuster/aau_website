from django.urls import path
from .views import ProfileDetailView
from . import views


urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
