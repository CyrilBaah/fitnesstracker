from django.core.management.base import BaseCommand
from faker import Faker

from exercises.models import Exercises


class Command(BaseCommand):
    help = "Seeds the Exercise table with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        # create 100 exercises with fake data
        for i in range(100):
            exercise = Exercises(
                name=fake.word().capitalize(),
                type=fake.random_element(elements=("cardio", "strength", "flexibility")),
                description=fake.sentence(),
                user_id=fake.random_int(min=1, max=3),  # Assuming 10 users with IDs 1-10
            )
            exercise.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded Exercise table"))
