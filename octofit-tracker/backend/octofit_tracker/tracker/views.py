from django.contrib.auth.models import User
from rest_framework import viewsets

from octofit_tracker.tracker.models import Activity, Leaderboard, Team, WorkoutSuggestion
from octofit_tracker.tracker.serializers import (
    ActivitySerializer,
    LeaderboardSerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSuggestionSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related("members").all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related("user").all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.select_related("user", "team").all()
    serializer_class = LeaderboardSerializer


class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all()
    serializer_class = WorkoutSuggestionSerializer