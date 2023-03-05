from django.urls import path
from .views import HomePageView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail-view'),
]