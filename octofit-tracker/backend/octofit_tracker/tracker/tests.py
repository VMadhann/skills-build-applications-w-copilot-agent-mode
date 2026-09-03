from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from octofit_tracker.tracker.models import Activity, Team


class TrackerApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test-user", email="test@example.com")
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)

    def test_root_points_to_api_resources(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["activities"], "/api/activities/")

    def test_activity_endpoint_lists_activities(self):
        Activity.objects.create(
            user=self.user,
            activity_type="running",
            duration_minutes=20,
            points=40,
            completed_at="2025-01-15T12:00:00Z",
        )
        response = self.client.get(reverse("activity-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]["points"], 40)

    def test_api_exposes_all_collections(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.json()), {"users", "teams", "activities", "leaderboard", "workouts"})