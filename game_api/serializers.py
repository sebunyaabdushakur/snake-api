from rest_framework import serializers
from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ["id", "player_name", "score", "level", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_level(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Level must be between 1 and 5."
            )
        return value
