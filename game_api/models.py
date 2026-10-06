from django.db import models


class Score(models.Model):
    player_name = models.CharField(max_length=50, default="Player")
    score = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player_name}: {self.score}"
