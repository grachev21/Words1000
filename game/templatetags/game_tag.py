from django import template
from settings.models import WordsSettings
from users.models import WordsUser

register = template.Library()


@register.inclusion_tag("includes/progress_bar_game.html", takes_context=True)
def progress_bar_game(context):

    study = WordsUser.objects.filter(user=context["user"], status=2).count()
    studied = WordsSettings.objects\
        .filter(
            user=context["user"]).latest("id").number_words - study

    print(study, studied)
    return {
        "progress": round(((study - studied) / study) * 100) - 100,
        "remainder": study}
