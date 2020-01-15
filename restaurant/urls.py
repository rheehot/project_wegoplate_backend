from django.urls import path
from .views       import TopTopic, RestaurantView, DetailTopImage, RestaurantDetailInfoView, RestaurantDetailToplistView, RestaurantNearView, DetailReview

urlpatterns = [
    path('/topic/<int:topic_id>', TopTopic.as_view()),
    path('/<int:topic_id>', RestaurantView.as_view()),
    path('/<int:restaurant_id>/topimage', DetailTopImage.as_view()),
    path('/<int:restaurant_id>/info', RestaurantDetailInfoView.as_view()),
    path('/<int:restaurant_id>/toplist', RestaurantDetailToplistView.as_view()),
    path('/<int:restaurant_id>/review', DetailReview.as_view()),
    path('/<int:restaurant_id>/near', RestaurantNearView.as_view()),
]
