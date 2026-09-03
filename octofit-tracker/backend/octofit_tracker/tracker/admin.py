from django.contrib import admin

from octofit_tracker.tracker.models import Activity, Leaderboard, Team, WorkoutSuggestion


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    filter_horizontal = ["members"]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ["user", "activity_type", "duration_minutes", "points", "completed_at"]
    list_filter = ["activity_type"]


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ["rank", "user", "team", "total_points", "updated_at"]
    list_filter = ["team"]


@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ["title", "activity_type", "difficulty", "min_points"]
    list_filter = ["activity_type", "difficulty"]