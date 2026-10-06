from django.urls import path
from .views import ScoreListCreateView, game_page

urlpatterns = [
    path("", game_page, name="game-page"),
    path("scores/", ScoreListCreateView.as_view(), name="score-list"),
]
