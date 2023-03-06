from django.urls import path
from .views import HomePageView, PostDetailView, art_category, fashion_category, music_category, brand_category

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>', PostDetailView.as_view(), name='post-detail-view'),
    path('category/art/', art_category, name='art-category' ),
    path('category/fashion/', fashion_category, name='fashion-category' ),
    path('category/music/', music_category, name='music-category' ),
    path('category/brand/', brand_category, name='brand-category' ),
]