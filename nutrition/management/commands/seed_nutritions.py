from django.core.management.base import BaseCommand
from faker import Faker

from nutrition.models import Nutrition


class Command(BaseCommand):
    help = "Seeds the nutrition table with fake data"

    def handle(self, *args, **options):
        fake = Faker()

        # create 100 nutritions with fake data
        for i in range(100):
            nutrition = Nutrition(
                name=fake.word().capitalize(),
                food_type=fake.random_element(
                    elements=("breakfast", "lunch", "dinner", "snack")
                ),
                calorie_count=fake.random_int(min=2, max=79),
                user_id=fake.random_int(
                    min=1, max=3
                ),  # Assuming 10 users with IDs 1-10
            )
            nutrition.save()

        self.stdout.write(self.style.SUCCESS("Successfully seeded Nutrition table"))
