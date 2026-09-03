from datetime import datetime

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

from octofit_tracker.tracker.models import Activity, Team, WorkoutSuggestion


class Command(BaseCommand):
    help = "Create the OctoFit schema and idempotent sample data."

    def handle(self, *args, **options):
        self.stdout.write("Applying database migrations...")
        from django.core.management import call_command

        call_command("migrate", verbosity=0)

        users = []
        for username, first_name in (("alex", "Alex"), ("jamie", "Jamie"), ("taylor", "Taylor")):
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"first_name": first_name, "email": f"{username}@example.com"},
            )
            users.append(user)
            if created:
                user.set_unusable_password()
                user.save(update_fields=["password"])

        team, _ = Team.objects.get_or_create(
            name="Mergington Movers",
            defaults={"description": "A friendly team for after-school fitness."},
        )
        membership_model = Team.members.through
        for user in users:
            membership_model.objects.get_or_create(team_id=team.pk, user_id=user.pk)

        sample_completed_at = timezone.make_aware(datetime(2025, 1, 15, 12, 0))
        activity_data = (
            (users[0], "running", 30, 60),
            (users[1], "walking", 45, 45),
            (users[2], "strength", 25, 50),
        )
        for user, activity_type, duration, points in activity_data:
            Activity.objects.get_or_create(
                user=user,
                activity_type=activity_type,
                completed_at=sample_completed_at,
                defaults={"duration_minutes": duration, "points": points},
            )

        suggestions = (
            ("Easy interval run", "running", "beginner", "Alternate one minute jogging with two minutes walking.", 0),
            ("Campus power walk", "walking", "beginner", "Walk briskly for 30 minutes and finish with a cool-down.", 0),
            ("Bodyweight circuit", "strength", "intermediate", "Complete three rounds of squats, push-ups, and lunges.", 40),
        )
        for title, activity_type, difficulty, description, min_points in suggestions:
            WorkoutSuggestion.objects.update_or_create(
                title=title,
                defaults={
                    "activity_type": activity_type,
                    "difficulty": difficulty,
                    "description": description,
                    "min_points": min_points,
                },
            )

        self.stdout.write(self.style.SUCCESS("OctoFit database initialized with sample users, team, activities, and workouts."))