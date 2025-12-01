from django import template
from settings.models import WordsSettings
from users.models import WordsUser

register = template.Library()


@register.inclusion_tag("includes/progress_bar_game.html", takes_context=True)
def progress_bar_game(context):
    user = context["user"]
    words_user = WordsUser.objects.filter(user=user, status=2)
    words_settings = WordsSettings.objects.filter(user=user).latest("id")
    study = words_user.count()
    studied = words_settings.number_words - study
    print(study, studied)
    return {
        "progress": round(((study - studied) / study) * 100) - 100,
        "remainder": study,
    }
