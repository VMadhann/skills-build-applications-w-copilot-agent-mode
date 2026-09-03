from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from octofit_tracker.tracker.views import (
	ActivityViewSet,
	LeaderboardViewSet,
	TeamViewSet,
	UserViewSet,
	WorkoutSuggestionViewSet,
)


router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("teams", TeamViewSet, basename="team")
router.register("activities", ActivityViewSet, basename="activity")
router.register("leaderboard", LeaderboardViewSet, basename="leaderboard")
router.register("workouts", WorkoutSuggestionViewSet, basename="workout")


def api_root(request):
	return JsonResponse({"users": "/api/users/", "teams": "/api/teams/", "activities": "/api/activities/", "leaderboard": "/api/leaderboard/", "workouts": "/api/workouts/"})


urlpatterns = [
	path("", api_root, name="api-root"),
	path("admin/", admin.site.urls),
	path("api/", api_root, name="api-root-api"),
	path("api/", include(router.urls)),
]