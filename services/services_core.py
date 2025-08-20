import random
from core.models import WordsCard
from users.models import WordsUser


def create_records_signals(user, quantity):
    if WordsUser.objects.filter(user=user).exists():
        random_elements = random.sample(WordsCard.objects.all(), quantity)
        for element in random_elements:
            WordsUser.objects.create(
                user=user,
                core_words=element,
            )
