from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name="fitness_teams", blank=True)


class Activity(models.Model):
    ACTIVITY_TYPES = [("running", "Running"), ("walking", "Walking"), ("strength", "Strength")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration_minutes = models.PositiveIntegerField()
    points = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField()


class WorkoutSuggestion(models.Model):
    title = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=20, choices=Activity.ACTIVITY_TYPES)
    difficulty = models.CharField(max_length=20)
    description = models.TextField()
    min_points = models.PositiveIntegerField(default=0)


class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leaderboard_entries")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="leaderboard_entries")
    total_points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["rank", "-total_points"]
        constraints = [
            models.UniqueConstraint(fields=["user", "team"], name="unique_leaderboard_user_team"),
        ]