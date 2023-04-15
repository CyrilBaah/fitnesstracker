import random
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

from workout.models import Workout

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the workout table with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        for i in range(100):
            user = User.objects.get(id=fake.random_int(min=1, max=3))
            workout = Workout(
                date=fake.date_between(start_date="-30d", end_date="today"),
                time=fake.time(),
                duration=timedelta(minutes=random.randint(30, 120)),
                user=user,
            )
            workout.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded Nutrition table"))
