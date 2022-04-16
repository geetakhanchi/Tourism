from django.urls import path
from .views import TourList, TourDetail


urlpatterns = [
    path('<int:pk>/', TourDetail.as_view()),
    path('', TourList.as_view()),
]