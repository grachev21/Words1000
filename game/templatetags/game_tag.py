from django import template
# from settings.models import WordsSettings
from users.models import WordsUser

register = template.Library()


@register.inclusion_tag("includes/progress_bar_game.html", takes_context=True)
def progress_bar_game(context):

    study = WordsUser.objects.filter(status=2, user=context["user"]).count()
    studied = WordsUser.objects.filter(status=4, user=context["user"]).count()

    result = ((study - studied) / 100) * 100

    result = round(result, 2)
    print(study)
    print(studied)
    print(context["user"])
    print(result)

    return {}
