from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='TestTeam')
        self.assertEqual(str(t), 'TestTeam')

    def test_user_create(self):
        team = Team.objects.create(name='TestTeam')
        u = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        self.assertEqual(u.username, 'testuser')
        self.assertEqual(u.team, team)

    def test_activity_create(self):
        team = Team.objects.create(name='TestTeam')
        u = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        a = Activity.objects.create(user=u, type='run', duration=10, distance=2.5)
        self.assertEqual(a.user, u)

    def test_workout_create(self):
        w = Workout.objects.create(name='TestWorkout', description='desc')
        self.assertEqual(w.name, 'TestWorkout')

    def test_leaderboard_create(self):
        team = Team.objects.create(name='TestTeam')
        l = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(l.team, team)
