from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Workout.objects.all():
            obj.delete()
        for obj in Leaderboard.objects.all():
            obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2025-12-01')
        Activity.objects.create(user=captain, type='Cycling', duration=45, calories=400, date='2025-12-01')
        Activity.objects.create(user=superman, type='Swimming', duration=60, calories=500, date='2025-12-01')
        Activity.objects.create(user=batman, type='Yoga', duration=20, calories=100, date='2025-12-01')

        # Create workouts
        cardio = Workout.objects.create(name='Cardio', description='Cardio workout')
        strength = Workout.objects.create(name='Strength', description='Strength workout')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(marvel, dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=700)
        Leaderboard.objects.create(team=dc, points=600)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
