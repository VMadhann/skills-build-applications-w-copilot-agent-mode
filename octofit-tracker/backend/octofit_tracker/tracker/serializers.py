from django.contrib.auth.models import User
from rest_framework import serializers

from octofit_tracker.tracker.models import Activity, Leaderboard, Team, WorkoutSuggestion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Team
        fields = ["id", "name", "description", "members"]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "points", "completed_at"]


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ["id", "user", "team", "total_points", "rank", "updated_at"]
        read_only_fields = ["updated_at"]


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = ["id", "title", "activity_type", "difficulty", "description", "min_points"]