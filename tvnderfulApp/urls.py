from django.urls import path
from .views import series_list, episode_detail

urlpatterns = [
    path('list/', series_list, name="series_list"),
    path('detail/<int:id>/', episode_detail, name="episode_detail"),
]
