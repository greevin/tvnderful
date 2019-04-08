from django.urls import path
from .views import series_list, episode_detail, show_index

urlpatterns = [
    path('show/<int:id>', series_list, name="show_list"),
    path('detail/<int:id>/', episode_detail, name="episode_detail"),
    path('', show_index, name="show_index")
]
