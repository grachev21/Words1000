from words.models import WordsCard

for w in WordsCard.objects.all():
    print(w)
