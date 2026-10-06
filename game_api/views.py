from django.shortcuts import render
from rest_framework import generics

from .models import Score
from .serializers import ScoreSerializer


class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.order_by("-created_at")
    serializer_class = ScoreSerializer


def game_page(request):
    return render(request, "game_api/index.html")
